from unittest import TestCase, main

from linkedin_searcher.searcher import LinkedInSearcher

class DatabaseStub():
    def __init__(self):
        self.database = {}

    def add_user(self, user):
        self.database[user.username] = user

    def search_user(self, query_dict):
        return [self.database[query_dict.get('username')]]

class SearcherTester(TestCase):
    def _make_and_fill_searcher(self):
        database = DatabaseStub()
        searcher = LinkedInSearcher(database)
        searcher.add_public_profile(self._make_test_user_attributes())
        return searcher

    def _make_test_user_attributes(self):
        return {
            'username': '0',
            'name': 'a', 
            'title': 'b', 
            'position': 'cat', 
            'summary': 'dog', 
            'skills': 'e', 
            'experience': 1, 
            'education': 2
        }

    def test_search_profiles(self):
        searcher = self._make_and_fill_searcher()
        output = searcher.search_profiles({'username': '0'})
        true_output = self._make_test_user_attributes()
        true_output['skills'] = ['e']
        true_output['score'] = 3
        assert output == [true_output]

if __name__ == '__main__':
    main()