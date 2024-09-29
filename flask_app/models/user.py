from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
import base64

class User:
    DB = 'DnD'
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.profile_picture = data['profile_picture']
        if self.profile_picture:
            self.profile_picture = base64.b64encode(self.profile_picture).decode('utf-8')

    def html_profpic(self):
        if self.profile_picture:
            return f'<img src="data:image/jpeg;base64,{self.profile_picture}" alt="Profile Picture" />'
        else:
            return '<p>No profile picture available.</p>'

    @classmethod
    def new_user(cls, data):
        query = """ INSERT INTO users(username, profile_picture)
                    VALUES(%(username)s, %(profile_picture)s)
                """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_one(cls, id):
        data = {'id': id}
        query = """ SELECT * FROM users
                    WHERE id = %(id)s
                """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result[0]

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM users"""
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for result in results:
            users.append(cls(result))
        return users
    
    @classmethod
    def edit_user(cls, data):
        query = """ UPDATE users
                    SET username = %(username)s, profile_picture = %(profile_picture)s
                    WHERE id = %(id)s
                """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_user(cls, id):
        query = """ DELETE FROM users 
                    WHERE id = %(id)s
                """
        data = {'id': id}
        return connectToMySQL(cls.DB).query_db(query, data)
