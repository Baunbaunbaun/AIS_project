### SHORE DB ###
import db

# create db
shore_db, shore_cursor = db.create_DB('shore')
# create table
db.create_msg_table(shore_db, shore_cursor)

def insert(msg):
    key, slot, mmsi, timestamp, x, y = msg
    db.insert(shore_db, shore_cursor, key, slot, mmsi, timestamp, x, y)

def insert_lst(lst):
    print('SDB: inserting list in DB')
    for msg in lst[1]: 
        try:
            insert(msg)
        except:
            continue
 
# return all mmsi from list, that is not in shore_db in specific slot
def get_mmsi_not_in_slot(lst): # [slot, [mmsi_lst]]
    return db.get_mmsi_not_in_slot(shore_cursor, lst)










 # dublet rows in DB FN
def has_mmsi_in_slot(mmsi, slot):
    mmsi_lst = db.get_specific_mmsi_in_slot(shore_cursor, mmsi, slot)
    print("getting ", mmsi, " in ", slot)    
    return len(mmsi_lst)>0


def print_db():
    db.printRows(shore_cursor)

def get_size():
    return db.get_size(shore_cursor)

def get_top_3():  
    return db.get_top_3(shore_cursor)

def check_menu(menu):
    slot = menu[0]
    mmsi_lst = menu[1]
    # logic here
    request_lst = []
    return request_lst


"""

# testing DB operations

shore_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables in DB: ", shore_cursor.fetchall())

# INSERT
for i in range(10):
    input = str(i), str(i), i, i, float(i), float(i)
    insert(input)

msg_test_lst = []
for i in range(10,20):
    input = str(i), str(i), i, i, float(i), float(i)
    msg_test_lst.append(input)

print(msg_test_lst)

print_db()

print("Size:", get_size())

top3 = [0,1,2]
top3msg = get_top_3()
# print(top3msg)
insert_lst(msg_test_lst)

print_db()

print(get_mmsi_not_in_slot(top3, 1))

# print(has_mmsi_in_slot(9,7))

#print(get_specific_mmsi_in_slot("(1,2,3)", 5))

"""