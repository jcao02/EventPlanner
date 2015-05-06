from flask import g
from base import get_database

TABLENAME = 'User'

class User:
    user     = ""
    password = ""
    def __init__(self, data):
        self.user     = data['user']
        self.password = data['password']

    def save(self): 
        database = get_database()
        cursor   = database.cursor()
        try: 
            sql_request = 'INSERT INTO %s (username, password) VALUES ("%s", "%s")' % ( TABLENAME, self.user, self.password )

            print " "
            print sql_request
            print " "
            cursor.execute(sql_request)
            database.commit()
            return True
        except Exception as e: 
            database.rollback()
            print e.message
            return False

    def exists(self):
            sql_request = 'SELECT username FROM %s' % TABLENAME
            print " "
            print sql_request
            print " "

            database = get_database()
            cursor   = database.cursor()

            cursor.execute(sql_request)
            user = cursor.fetchone()
            return user and len(user) > 0

    def authenticate(self):
            sql_request = 'SELECT username FROM %s WHERE username="%s" AND password="%s"' % ( TABLENAME, self.user, self.password )
            print " "
            print sql_request
            print " "

            database = get_database()
            cursor   = database.cursor()

            cursor.execute(sql_request)
            user = cursor.fetchone()
            return user and len(user) > 0

