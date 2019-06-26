import json

from linkedin_searcher.models.user import User

class LinkedInSearcher:

    def __init__(self, database):
        self.database = database

    def add_public_profile(self, user_attributes):
        linkedin_user = User(
            user_attributes.get('username'),
            user_attributes.get('name'),
            user_attributes.get('title'),
            user_attributes.get('position'),
            user_attributes.get('summary'),
            user_attributes.get('skills'),
            user_attributes.get('experience'),
            user_attributes.get('education')
        )
        self.database.add_user(linkedin_user)  

    def search_profiles(self, query_dict):
        user_list = self.database.search_user(query_dict)
        return self._make_user_data_list(user_list)
    
    def _make_user_data_list(self, user_list):
        user_data_list = []
        for user in user_list:
            user_data_list.append(user.get_data_dict())
        return user_data_list
