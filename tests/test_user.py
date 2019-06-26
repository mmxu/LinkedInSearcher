from unittest import TestCase, main

from linkedin_searcher.models.user import User

class UserTester(TestCase):

    def _make_sample_output(self):
        return {
            'username': 'username',
            'name': 'name',
            'title': 'title',
            'position': 'position',
            'summary': 'summary',
            'experience': 1,
            'education': 2,
            'score': 3
        }

    def test_user_one_skill(self):
        test_user = User(
            'username',
            'name',
            'title',
            'position',
            'summary',
            'skills',
            1,
            2
        )
        output = test_user.get_data_dict()
        true_output = self._make_sample_output()
        true_output['skills'] = ['skills']
        assert output == true_output

    def test_user_two_skills(self):
        test_user = User(
            'username',
            'name',
            'title',
            'position',
            'summary',
            'skill1,skill2',
            1,
            2
        )
        output = test_user.get_data_dict()
        true_output = self._make_sample_output()
        true_output['skills'] = ['skill1', 'skill2']
        assert output == true_output

if __name__ == '__main__':
    main()