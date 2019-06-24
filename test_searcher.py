from unittest import mock

import searcher

def mock_init(self):
    self.database = searcher.userdatabase.sqlite3.connect(':memory:')
    self.cursor = self._make_cursor()
    self._create_table_if_needed()

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

def test_search_profiles_one_user():
    linkedin_searcher = _make_and_fill_searcher()
    output = linkedin_searcher.search_profiles({'name': 'a'})
    assert output == [_make_test_user_a_return()]

@mock.patch.object(searcher.userdatabase.UserDatabase, '__init__', mock_init)
def _make_and_fill_searcher():
    linkedin_searcher = searcher.LinkedInSearcher()
    linkedin_searcher.add_public_profile(_make_test_user_attributes_a())
    linkedin_searcher.add_public_profile(_make_test_user_attributes_b())
    return linkedin_searcher

def _make_test_user_attributes_a():
    return {
        'name':'a', 
        'title':'b', 
        'position':'cat', 
        'summary':'dog', 
        'skills':'e,f,g', 
        'experience':1, 
        'education':2
    }

def _make_test_user_attributes_b():
    return {
        'name':'1', 
        'title':'2', 
        'position':'cat', 
        'summary':'dog', 
        'skills':'5,6,7', 
        'experience':8, 
        'education':9
    }

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

def test_search_profiles_two_users():
    linkedin_searcher = _make_and_fill_searcher()
    output = linkedin_searcher.search_profiles({'position': 'cat'})
    assert output == [
        _make_test_user_a_return(), _make_test_user_b_return()
    ]

if __name__ == '__main__':
    test_search_profiles_one_user()
    test_search_profiles_two_users()
    print("All tests passed.")