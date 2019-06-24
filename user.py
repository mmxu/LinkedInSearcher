class User:

    # takes a dict as user_attributes
    def __init__(self, user_attributes):
        self.user_data = user_attributes.copy()
        self._calculate_score_if_applicable()
        
    def _calculate_score_if_applicable(self):
        if self._can_calculate_score():
            print(self.user_data['experience'])
            print(type(self.user_data['experience']))
            self.user_data['score'] = int(self.user_data['experience']) + int(self.user_data['education'])

    def _can_calculate_score(self):
        return 'experience' in self.user_data and 'education' in self.user_data
    
    def get_data(self):
        return self.user_data
