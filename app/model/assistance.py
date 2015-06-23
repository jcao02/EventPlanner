from flask import g
from base import get_database

TABLENAME = "Assitance"
class Assistance:
    user  = ""
    event = -1
    assisted = 0

    def __init__(self, user, event, assisted=0):
        self.user     = user
        self.event    = event
        self.assisted = assisted

    def save(self): 
        database = get_database()
        cursor   = database.cursor()
        try: 
            sql_request = 'INSERT INTO %s (participant, event, assited) \
				VALUES ("%s", "%s", 0)' % ( TABLENAME, self.user, self.event )

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
    
    def delete(self):
        sql_request = 'DELETE FROM %s WHERE participant="%s" AND event="%s"' % (TABLENAME,self.user,self.event)
        print " "
        print sql_request
        print " "
        try: 
            database = get_database()
            cursor   = database.cursor()
            cursor.execute(sql_request)
            database.commit()
            return True
        except Exception as e: 
            database.rollback()
            print e.message
            return False


    @staticmethod
    def get(user, event):
        sql_request = 'SELECT participant,event,assited FROM %s WHERE participant="%s" AND event="%s"' % (TABLENAME,user,event)
        print " "
        print sql_request
        print " "

        database = get_database()
        cursor   = database.cursor()
        cursor.execute(sql_request)

        row = cursor.fetchone()

        if row is None:
            return None
        else:
            assistance = Assistance(row[0], int(row[1]), int(row[2]))
            return assistance


