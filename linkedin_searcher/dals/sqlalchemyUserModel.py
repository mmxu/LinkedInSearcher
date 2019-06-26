from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from linkedin_searcher.models.user import User

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    name = Column(String)
    title = Column(String)
    position = Column(String)
    summary = Column(String)
    skills = Column(String)
    experience = Column(Integer)
    education = Column(Integer)

    def check_if_exists_and_create_table(self, engine):
        Base.metadata.create_all(engine)

    def make_user_object(self):
        return User(
            self.username,
            self.name,
            self.title,
            self.position,
            self.summary, 
            self.skills,
            self.experience,
            self.education
        )

    