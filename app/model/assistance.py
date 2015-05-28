TABLENAME = "Assitance"
class Assistance:
    user  = ""
    event = -1

    def __init__(self, user, event):
        self.user  = user
        self.event = event

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

    @staticmethod
    def get(user, event):
        sql_request = 'SELECT * FROM %s WHERE participant="%s" AND event="%s"' % (TABLENAME,user,event)
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
            assistance = Assistance(row[0], int(row[1]))
            return assistance


