user_attributes = [
    'name', 'title', 'position', 'summary', 
    'skills', 'experience', 'education', 'score'
]

user_attribute_types = [
    'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 
    'INTEGER', 'INTEGER', 'INTEGER'
]

searchable_attributes = [
    'name', 'title', 'position', 'summary', 'skills'
]

def make_creation_statement():
    creation_list = []
    for i in range(len(user_attributes)):
        creation_list.append(user_attributes[i] + " " + user_attribute_types[i])
    creation_string = ", ".join(creation_list)
    return "CREATE TABLE users(" + creation_string + ")"

def make_insert_statement(user_data_dict):
    return (_make_insert_string(), _make_user_data_list(user_data_dict))

def _make_insert_string():
    attribute_string = ", ".join(user_attributes)
    values_string = ", ".join(["?" for i in range(len(user_attributes))])
    return "INSERT INTO users(" + attribute_string + ") VALUES(" + values_string + ")"

def _make_user_data_list(user_data_dict):
    return [user_data_dict.get(attribute) for attribute in user_attributes]

def make_return_statement(user_list):
    user_dict_list = []
    for user_data_tuple in user_list:
        user_dict = {}
        for i in range(len(user_attributes)):
            user_dict[user_attributes[i]] = user_data_tuple[i]
        user_dict_list.append(user_dict)
    return _format_user_dict_list(user_dict_list)

def _format_user_dict_list(user_dict_list):
    for user_dict in user_dict_list:
        user_dict['skills'] = user_dict['skills'].split(",")
    return user_dict_list

def make_query_statement(query_dict):
    query_list = []
    for attribute in searchable_attributes:
        if attribute in query_dict:
            query_list.append(attribute + " LIKE '%" + str(query_dict[attribute]) + "%'")
    query_string = " AND ".join(query_list)
    return "SELECT * FROM users WHERE " + query_string