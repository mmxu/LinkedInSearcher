from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from linkedin_searcher.dals.sqlalchemyUserModel import UserModel
from linkedin_searcher.models.user import User

class UserDatabase():
    def __init__(self, conn_string: str):
        self._conn_string = conn_string
        self._engine = create_engine(self._conn_string)
        self._session_maker = sessionmaker(bind=self._engine)
        self._create_table_if_needed()

    def _create_table_if_needed(self):
        user_model = UserModel()
        user_model.check_if_exists_and_create_table(self._engine)

    @contextmanager
    def _session_scope(self):
        session = self._session_maker()
        try:
            yield session
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def add_user(self, user: User):
        with self._session_scope() as session:
            user_model = UserModel(
                username=user.username,
                name=user.name,
                title=user.title,
                position=user.position,
                summary=user.summary,
                skills=user.skills,
                experience=user.experience,
                education=user.education
            )
            session.add(user_model)
            session.commit()

    def search_user(self, query_dict: dict):
        with self._session_scope() as session:
            users_found = session.query(UserModel)
            users_found_filtered = self._filter_query(users_found, query_dict)
            user_model_list = users_found_filtered.all()
            user_list = self._make_user_list(user_model_list)
            return(user_list)

    def _filter_query(self, users_found, query_dict):
        for parameter in query_dict.keys():
            attribute = getattr(UserModel, parameter)
            query_string = '%' + query_dict[parameter] + '%'
            users_found = users_found.filter(attribute.like(query_string))
        return users_found

    def _make_user_list(self, user_model_list):
        user_list = []
        for user_model in user_model_list:
                user_list.append(user_model.make_user_object())
        return user_list
