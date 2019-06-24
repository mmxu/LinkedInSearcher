import user

def test_user_no_score():
    test_user = user.User({'name':'a'})
    assert test_user.get_data() == {'name':'a'}

def test_user_with_score():
    experience = 5
    education = 1000
    test_user = user.User({'experience': experience, 'education': education})
    assert test_user.get_data() == {'experience': experience, 'education': education, 'score': experience + education}

if __name__ == '__main__':
    test_user_no_score()
    test_user_with_score()
    print("All tests passed.")