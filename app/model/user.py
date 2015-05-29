from flask import g
from base import get_database

TABLENAME = 'User'
ASSISTANCE_TABLENAME = 'Assitance'
EVENT_TABLENAME = 'Event'

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

    @staticmethod
    def all():
        sql_request = 'SELECT username FROM %s' % (TABLENAME)
        print " "
        print sql_request
        print " "

        database = get_database()
        cursor   = database.cursor()

        cursor.execute(sql_request)

        users = cursor.fetchall()

        users = map(lambda x: x[0], users)
        return users

    @staticmethod
    def from_event(event):
    
        sql_request = 'SELECT participant FROM %s WHERE event="%s"' % ( ASSISTANCE_TABLENAME, event )
        print " "
        print sql_request
        print " "
           

        database = get_database()
        cursor   = database.cursor()

        cursor.execute(sql_request2)
        cursor.execute(sql_request)

        users = cursor.fetchall()
        users = map(lambda x: x[0], users)
        return users

    @staticmethod
    def get(username):
        sql_request = 'SELECT * FROM %s WHERE username="%s"' % (TABLENAME,username)
        print " "
        print sql_request
        print " "

        database = get_database()
        cursor   = database.cursor()
        cursor.execute(sql_request)

        user_row = cursor.fetchone()

        if user_row is None:
            return None
        else:
            user_data = {'user': user_row[0],
                         'password': user_row[1]
                        }

            userid = User(user_data).__dict__
            return userid


    @staticmethod
    def get_assisted(username):
        sql_request = 'SELECT event FROM %s WHERE participant="%s"' % (ASSISTANCE_TABLENAME,username)
        print " "
        print sql_request
        print " "

        database = get_database()
        cursor   = database.cursor()
        cur   = database.cursor()
        cursor.execute(sql_request)

        assited_data = []

        user_row = cursor.fetchone()

        if user_row is None:
            return None

        while (user_row <> None):
            sql_request3 = 'SELECT name FROM %s WHERE eventid="%s"' % (EVENT_TABLENAME,user_row[0])
            cur.execute(sql_request3)
            event_name = cur.fetchone()

            assited_data.append((event_name[0], user_row[0]))
            user_row = cursor.fetchone()
        
        #data = User(assited_data).__dict__
        return assited_data

    @staticmethod
    def get_created(username):
        sql_request = 'SELECT name, eventid FROM %s WHERE owner="%s"' % (EVENT_TABLENAME,username)
        print " "
        print sql_request
        print " "

        database = get_database()
        cursor   = database.cursor()
        cursor.execute(sql_request)

        created_data = []

        user_row = cursor.fetchone()

        if user_row is None:
            return None

        
        while (user_row <> None):
            created_data.append((user_row[0],user_row[1]))
            user_row = cursor.fetchone()
        
        #data = User(created_data).__dict__
        return created_data

