import sqlite_statement_maker as sql_helper

def test_make_creation_statement():
    output = sql_helper.make_creation_statement()
    true_output = (
        "CREATE TABLE users(name TEXT, title TEXT, position TEXT, summary TEXT, " 
        "skills TEXT, experience INTEGER, education INTEGER, score INTEGER)"
    )
    assert output == true_output

def test_make_insert_statement_string():
    output = sql_helper.make_insert_statement(_make_test_user())[0]
    true_output = (
        "INSERT INTO users(name, title, position, summary, skills, experience, "
        "education, score) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
    )
    assert output == true_output

def _make_test_user():
    return {
        'name':'a',
        'title':'b',
        'position':'c',
        'summary':'d',
        'skills':'e',
        'experience':1,
        'education':2,
        'score':3
    }

def test_make_insert_statement_list():
    output = sql_helper.make_insert_statement(_make_test_user())[1]
    assert output == ['a', 'b', 'c', 'd', 'e', 1, 2, 3]

def test_make_return_statement_one_user():
    user_list = [('a', 'b', 'c', 'd', 'e', 1, 2, 3)]
    output = sql_helper.make_return_statement(user_list)
    assert output == [_make_test_return_user()]

def _make_test_return_user():
    return {
        'name':'a',
        'title':'b',
        'position':'c',
        'summary':'d',
        'skills':['e'],
        'experience':1,
        'education':2,
        'score':3
    }

def test_make_return_statement_two_users():
    user_list = [('a', 'b', 'c', 'd', 'e', 1, 2, 3),('a', 'b', 'c', 'd', 'e', 1, 2, 3)]
    output = sql_helper.make_return_statement(user_list)
    assert output == [_make_test_return_user(), _make_test_return_user()]

def test_make_query_statement_one_attribute():
    output = sql_helper.make_query_statement({'name':'a'})
    true_output = "SELECT * FROM users WHERE name LIKE '%a%'"
    assert output == true_output

def test_make_query_statement_two_attributes():
    output = sql_helper.make_query_statement({'name':'a', 'title':'b'})
    true_output = "SELECT * FROM users WHERE name LIKE '%a%' AND title LIKE '%b%'"
    assert output == true_output

if __name__ == '__main__':
    test_make_creation_statement()
    test_make_insert_statement_string()
    test_make_insert_statement_list()
    test_make_return_statement_one_user()
    test_make_return_statement_two_users()
    test_make_query_statement_one_attribute()
    test_make_query_statement_two_attributes()
    print("All tests passed.")