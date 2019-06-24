import sqlite3
from unittest import mock

import userdatabase

def mock_init(self):
    self.database = sqlite3.connect(':memory:')
    self.cursor = self._make_cursor()
    self._create_table_if_needed()

@mock.patch.object(userdatabase.UserDatabase, '__init__', mock_init)
def _create_and_fill_database():
    database = userdatabase.UserDatabase()
    database.add_user(_make_test_user_a())
    database.add_user(_make_test_user_b())
    return database

def _make_test_user_a():
    return {
        'name':'a', 
        'title':'b', 
        'position':'cat', 
        'summary':'dog', 
        'skills':'e,f,g', 
        'experience':1, 
        'education':2, 
        'score':3
    }

def _make_test_user_b():
    return {
        'name':'1', 
        'title':'2', 
        'position':'cat', 
        'summary':'dog', 
        'skills':'5,6,7', 
        'experience':8, 
        'education':9, 
        'score':17
    }

def test_search_one_user_with_one_attribute():
    database = _create_and_fill_database()
    output = database.search_user({'name': 'a'})
    assert output == [_make_test_user_a_return()]

def _make_test_user_a_return():
    return {
        'name':'a', 
        'title':'b', 
        'position':'cat', 
        'summary':'dog', 
        'skills':['e','f','g'], 
        'experience':1, 
        'education':2, 
        'score':3
    }

def test_search_one_user_with_two_attributes():
    database = _create_and_fill_database()
    output = database.search_user({'name': 'a', 'title':'b'})
    assert output == [_make_test_user_a_return()]

def test_search_two_users_with_one_attribute():
    database = _create_and_fill_database()
    output = database.search_user({'position': 'cat'})
    assert output == [
        _make_test_user_a_return(), _make_test_user_b_return()
    ]

def _make_test_user_b_return():
    return {
        'name':'1', 
        'title':'2', 
        'position':'cat', 
        'summary':'dog', 
        'skills':['5','6','7'], 
        'experience':8, 
        'education':9, 
        'score':17
    }

def test_search_two_users_with_two_attributes():
    database = _create_and_fill_database()
    output = database.search_user({'position': 'cat', 'summary': 'dog'})
    assert output == [
       _make_test_user_a_return(), _make_test_user_b_return()
    ]

def test_search_users_with_partial_match():
    database = _create_and_fill_database()
    output = database.search_user({'position': 'c', 'summary': 'd'})
    assert output == [
        _make_test_user_a_return(), _make_test_user_b_return()
    ]

if __name__ == '__main__':
    test_search_one_user_with_one_attribute()
    test_search_one_user_with_two_attributes()
    test_search_two_users_with_one_attribute()
    test_search_two_users_with_two_attributes()
    test_search_users_with_partial_match()
    print("All tests passed.")
