import sqlite3

import sqlite_statement_maker as sqlite_helper

class UserDatabase:

    def __init__(self):
        self.database = sqlite3.connect('linkedin_users.db', check_same_thread=False)
        self.cursor = self._make_cursor()
        self._create_table_if_needed()

    def _make_cursor(self):
        return self.database.cursor()

    def _create_table_if_needed(self):
        if self._table_does_not_exist():
            self.cursor.execute(sqlite_helper.make_creation_statement())
            self.database.commit()

    def _table_does_not_exist(self):
        self.cursor.execute(''' 
            SELECT count(name) FROM sqlite_master 
            WHERE type='table' AND name='users' 
        ''')
        return self.cursor.fetchone()[0] == 0

    def add_user(self, user_data_dict):
        self.cursor = self._make_cursor()
        insert_string, user_data_list = sqlite_helper.make_insert_statement(user_data_dict)
        self.cursor.execute(insert_string, user_data_list)
        self.database.commit()
    
    def search_user(self, query_dict):
        self.cursor = self._make_cursor()
        self.cursor.execute(sqlite_helper.make_query_statement(query_dict))
        user_list = self.cursor.fetchall()
        return sqlite_helper.make_return_statement(user_list)