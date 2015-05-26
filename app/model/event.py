from flask import g
from base import get_database

TABLENAME            = "Event"
ASSISTANCE_TABLENAME = 'Assitance'

# For the poster
UPLOAD_FOLDER      = './uploads/posters/'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

# Method to get the upload folder
def upload_folder():
    return UPLOAD_FOLDER
# Method to filter files extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Class Event
class Event:
    eventid        = -1
    name           = ""
    description    = ""
    poster_path    = ""
    event_date     = ""
    event_location = ""
    n_participants = 0
    owner          = ""

    def __init__(self, data):
        self.name           = data.get('name')
        self.description    = data.get('description')
        self.poster_path    = data.get('poster_path')
        self.event_date     = data.get('event_date')
        self.event_location = data.get('event_location')
        self.owner          = data.get('owner')

        if data.get('participants') != None:
            self.n_participants = int(data.get('participants'))

        if data.get('eventid') != None:
            self.eventid        = int(data.get('eventid'))

    def save(self): 
        database = get_database()
        cursor   = database.cursor()
        try: 
            sql_request = 'INSERT INTO %s (eventid, name, description, \
                    poster_path, event_date, event_location, n_participants, owner) \
                    VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % ( TABLENAME, self.name, self.description, 
                                                                                self.poster_path, self.event_date, 
                                                                                self.event_location, self.n_participants, 
                                                                                self.owner )

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
            event = cursor.fetchone()
            return event and len(event) > 0

    @staticmethod
    def get(eventid):
        sql_request = 'SELECT * FROM %s WHERE eventid="%s"' % (TABLENAME,eventid)
        print " "
        print sql_request
        print " "

        database = get_database()
        cursor   = database.cursor()
        cursor.execute(sql_request)

        event_row = cursor.fetchone()

        if event_row is None:
            return None
        else:
            event_data = {'eventid'         : int(event_row[0]), 
                          'name'            : event_row[1], 
                          'description'     : event_row[2], 
                          'poster_path'     : event_row[3], 
                          'event_date'      : event_row[4], 
                          'event_location'  : event_row[5], 
                          'participants'    : int(event_row[6]), 
                          'owner'           : event_row[7]
                        }

            event = Event(event_data).__dict__
            return event

    @staticmethod
    def all():
        sql_request = 'SELECT * FROM %s' % (TABLENAME)
        print " "
        print sql_request
        print " "

        database = get_database()
        cursor   = database.cursor()
        cursor.execute(sql_request)

        events_rows = cursor.fetchall()

        events_data = map(lambda x:
                {'eventid'         : int(x[0]),
                 'name'            : x[1],
                 'description'     : x[2],
                 'poster_path'     : x[3],
                 'event_date'      : x[4],
                 'event_location'  : x[5],
                 'participants'    : int(x[6]),
                 'owner'           : x[7]}, events_rows)
        
        events = map(lambda x: Event(x).__dict__, events_data)
        return events

    @staticmethod
    def all_owned_by(user):
        sql_request = 'SELECT * FROM %s WHERE owner="%s"' % (TABLENAME, user)
        print " "
        print sql_request
        print " "

        database = get_database()
        cursor   = database.cursor()
        cursor.execute(sql_request)

        events_rows = cursor.fetchall()
        events_data = map(lambda x:
                {'eventid'         : int(x[0]),
                 'name'            : x[1],
                 'description'     : x[2],
                 'poster_path'     : x[3],
                 'event_date'      : x[4],
                 'event_location'  : x[5],
                 'participants'    : int(x[6]),
                 'owner'           : x[7]}, events_rows)
        
        events = map(lambda x: Event(x).__dict__, events_data)
        return events



    @staticmethod
    def last_id():
        sql_request = 'SELECT eventid FROM %s ORDER BY eventid DESC LIMIT 1' % (TABLENAME)
        print " "
        print sql_request
        print " "

        database = get_database()
        cursor   = database.cursor()

        cursor.execute(sql_request)
        event = cursor.fetchone()

        return event[0] or None
