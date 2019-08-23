### SQLITE DB ###
import sqlite3

# instances of db and cursor
db = sqlite3.connect('data/none')
cursor = db.cursor()

# Creates/opens a file called aisDB with a SQLite3 DB
def create_DB(name):
    try:
        db = sqlite3.connect('data/'+name)
        cursor = db.cursor()
    except:
        pass

# create table
def createMsgTable():
    cursor.execute('DROP TABLE IF EXISTS messages')
    db.commit()

    cursor.execute('''
        CREATE TABLE messages(key TEXT PRIMARY KEY, slot INTEGER, mmsi INTEGER, timestamp TEXT, x FLOAT, y FLOAT)
        ''')
    db.commit()

# insert FN
def insert_db(key, slot, mmsi, timestamp, x, y):
    cursor.execute('''INSERT INTO messages(key, slot, mmsi, timestamp, x, y)
                  VALUES(?,?,?,?,?,?)''', (key, slot, mmsi, timestamp, x, y))
    db.commit()
 
# close FN
def close_db():
    db.close()

# print FN
def print_dict(dict):
    for d in dict.items():
        print(d)

# select mmsi in slot – DB FN
def getMMSIinSlot(slot):
    statement = 'SELECT * FROM messages WHERE slot = ' + str(slot) 
    cursor.execute(statement)
    print("getting MMSI messages from DB where slot = ",slot)    
    return cursor.fetchall()

# distinct rows in DB FN
def getAmountMMSI():
    cursor.execute('SELECT DISTINCT mmsi FROM messages ORDER BY key')
    print("getting distinct messages in DB")    
    return cursor.fetchall()
 
 # dublet rows in DB FN
def getDublets():
    cursor.execute('SELECT * FROM messages WHERE key IN (SELECT key FROM messages GROUP BY key HAVING COUNT(*) > 1) ORDER BY mmsi')
    print("getting dublet messages in DB")    
    return cursor.fetchall()