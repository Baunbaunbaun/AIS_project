### DB MODULE ###

# imports
import sqlite3

# variables
statement = ''
slot = -1
mmsi = -1
mmsi_lst = []
out = []

# functions
def create_DB(name):
    try:
        db = sqlite3.connect('data/'+name)
        cursor = db.cursor()
    except:
        pass
    return db, cursor

def create_msg_table(db, cursor):
    cursor.execute('DROP TABLE IF EXISTS messages')
    db.commit()

    cursor.execute('''
        CREATE TABLE messages(key TEXT PRIMARY KEY, slot INTEGER, mmsi INTEGER, timestamp TEXT, x FLOAT, y FLOAT)
        ''')
    db.commit()

def insert(db, cursor, key, slot, mmsi, timestamp, x, y):
    cursor.execute('''INSERT INTO messages(key, slot, mmsi, timestamp, x, y)
                  VALUES(?,?,?,?,?,?)''', (key, slot, mmsi, timestamp, x, y))
    db.commit()
 
def close_db(db):
    db.close()

# check mmsi in slot
# return [slot, [mmsi_lst]]
def get_mmsi_not_in_slot(cursor, lst): # [slot, [mmsi_lst]]
    slot = lst[0]
    mmsi_lst = lst[1]
    # check if slot is in DB
    statement = 'SELECT count(mmsi) FROM messages WHERE slot = ' + str(slot)
    cursor.execute(statement)
    out = cursor.fetchall()
    no_slot = out[0][0] == 0
    # if no slot, return lst
    if (no_slot): 
        # print('Result: ',lst)
        return lst

    out = [slot]

    # WHAT IS THIS ?
    statement = 'SELECT mmsi FROM messages WHERE slot = '  + str(slot) # + 'and mmsi not in ' + str(lst_to_tuple(mmsi_lst))
    
    cursor.execute(statement)
    res = tuples_to_values( cursor.fetchall() )
    res = lst_minus_lst(mmsi_lst,res)
    out.append(res)
    return out

def get_mmsi_in_slot(cursor, slot):
    out = [slot]
    statement = 'SELECT mmsi FROM messages WHERE slot = ' + str(slot) 
    cursor.execute(statement)
    out.append( list(tuples_to_values(cursor.fetchall())) ) 
    return out

def get_messages(cursor, lst): # [slot, [mmsi_lst]]
    slot = lst[0]
    mmsi_lst = lst[1]
    statement = 'SELECT * FROM messages WHERE (slot = ' + str(slot) + ' AND mmsi in ' + str(lst_to_tuple(mmsi_lst))+ ")" 
    cursor.execute(statement)
    out = [slot]
    res = cursor.fetchall()
    out.append(res)
    # extra lst element, to make it different from a [slot,[mmsi's]] lst
    out.append([])
    return out

def printRows(cursor):
    statement = 'SELECT * FROM messages'
    cursor.execute(statement)
    print('DB: Printing * from DB')  
    count = 0  
    for row in cursor.fetchall():
        print(count, row)
        count += 1

def get_size(cursor):
    statement = 'SELECT count(key) FROM messages'
    cursor.execute(statement)
    out = cursor.fetchall()
    size = out[0][0]
    return size  

def get_top_3(cursor):
    statement = 'SELECT * FROM messages LIMIT 3' 
    cursor.execute(statement)
    out = cursor.fetchall()
    print("DB: getting top 3 rows", out)    
    return out

# from list of tuples to list of values (SQLite returns list of tuples)
def tuples_to_values(tup):
    out = []
    for t in tup:
        out.append(t[0])
    return out

def lst_to_tuple(lst): 
    if(len(lst)==1):
        return "(" + str(lst[0]) + ")"
    return tuple(lst)

def lst_minus_lst(lst1,lst2):
    for v in lst2:
        try: 
            lst1.remove(v)
        except:
            continue
    return lst1