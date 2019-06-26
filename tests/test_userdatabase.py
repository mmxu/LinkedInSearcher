from unittest import TestCase, main

from linkedin_searcher.dals.userdatabase import UserDatabase
from linkedin_searcher.models.user import User

class DatabaseTester(TestCase):

    def _create_and_fill_database(self):
        database = UserDatabase('sqlite://')
        database.add_user(self._make_test_user_a())
        database.add_user(self._make_test_user_b())
        return database

    def _make_test_user_a(self):
        return User(
            username='1',
            name='a', 
            title='b', 
            position='cat', 
            summary='dog', 
            skills='e,f,g', 
            experience=1, 
            education=2 
        )

    def _make_test_user_b(self):
        return User(
            username='2',
            name='h', 
            title='i', 
            position='cat', 
            summary='dog', 
            skills='j,k', 
            experience=8, 
            education=9 
        )

    def test_search_one_user_with_one_attribute(self):
        database = self._create_and_fill_database()
        output = database.search_user({'name': 'a'})
        assert self._user_lists_are_equal(output, [self._make_test_user_a()])

    def _user_lists_are_equal(self, this_list, that_list):
        for i in range(len(this_list)):
            if this_list[i].get_data_dict() != that_list[i].get_data_dict():
                return False
        return True

    def test_search_one_user_with_two_attributes(self):
        database = self._create_and_fill_database()
        output = database.search_user({'name': 'a', 'title':'b'})
        assert self._user_lists_are_equal(output, [self._make_test_user_a()])

    def test_search_two_users_with_one_attribute(self):
        database = self._create_and_fill_database()
        output = database.search_user({'position': 'cat'})
        assert self._user_lists_are_equal(
            output, 
            [self._make_test_user_a(), self._make_test_user_b()]
        )

    def test_search_two_users_with_two_attributes(self):
        database = self._create_and_fill_database()
        output = database.search_user({'position': 'cat', 'summary': 'dog'})
        assert self._user_lists_are_equal(
            output, 
            [self._make_test_user_a(), self._make_test_user_b()]
        )

    def test_search_users_with_partial_match(self):
        database = self._create_and_fill_database()
        output = database.search_user({'position': 'c', 'summary': 'd'})
        assert self._user_lists_are_equal(
            output, 
            [self._make_test_user_a(), self._make_test_user_b()]
        )

if __name__ == '__main__':
    main()
