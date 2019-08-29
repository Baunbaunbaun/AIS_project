### DB MODULE ###

# imports
import sqlite3
import time

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
        print("DB initiation failed!")
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
def get_mmsi_not_in_slot(cursor, lst): # [slot, connection_level, [mmsi_lst]]

    if(len(lst)!=3): return []

    slot = lst[0]
    mmsi_lst = lst[2]

    # check if slot is represented in DB
    statement = 'SELECT count(mmsi) FROM messages WHERE slot = ' + str(slot)
    cursor.execute(statement)
    out = cursor.fetchall()
    no_slot = out[0][0] == 0
    # if no slot, return lst
    if (no_slot): 
        lst.pop(1)
        return lst

    avoid_lst = str(lst_to_tuple(mmsi_lst)) 

    statement = 'SELECT DISTINCT mmsi FROM messages WHERE slot = ' + str(slot) 
        
    cursor.execute(statement)
    res = tuples_to_values( cursor.fetchall() )
    print('distinct mmsi: ', res)
    res = lst_minus_lst(mmsi_lst,res)
    print('Shore is missing these mmsi in slot: ', res)

    out = [slot]
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
    return out

def printRows(cursor):
    statement = 'SELECT * FROM messages ORDER BY slot'
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
        while(True):
            try: 
                lst1.remove(v)
            except:
                break
    # this line is taken from – https://www.w3schools.com/python/python_howto_remove_duplicates.asp
    lst1 = list(dict.fromkeys(lst1))
    return lst1

# put a sequence of numbers in DB
# 2 rows pr 1 slot 
# slot numbers are always even
def test_data_in_db(db, cursor, amount):
    slots = []

    for i in range(amount):
        slots.append(i)
        for mmsi in range(int(amount/2)):
            key = time.time()
            try:
                insert(db, cursor, key, i, mmsi, float(i), float(i), float(i))
            except:
                continue

    for i in range(amount):
        slots.append(i)
        for mmsi in range(int(amount/2)):
            key = time.time()
            try:
                insert(db, cursor, key, i, mmsi, float(i), float(i), float(i))
            except:
                continue

    print('Test DB created')
    printRows(cursor)
    return slots

def delete(db,cursor,slot):
    cursor.execute('DELETE FROM messages WHERE slot = ' + str(slot))
    db.commit()