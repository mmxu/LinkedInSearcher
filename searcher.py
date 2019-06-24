import json

import user
import userdatabase

class LinkedInSearcher:

    def __init__(self):
        self.database = userdatabase.UserDatabase()

    def add_public_profile(self, user_attributes):
        linkedin_user = user.User(user_attributes)
        self.database.add_user(linkedin_user.get_data())  

    def search_profiles(self, query_dict):
        search_user = user.User(query_dict)
        return self.database.search_user(search_user.get_data())
