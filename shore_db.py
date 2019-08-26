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
    return lst[0]
 
# return all mmsi from list, that is not in shore_db in specific slot
def get_mmsi_not_in_slot(lst): # [slot, [mmsi_lst]]
    return db.get_mmsi_not_in_slot(shore_cursor, lst)

 # dublet rows in DB FN
def has_mmsi_in_slot(mmsi, slot):
    mmsi_lst = db.get_specific_mmsi_in_slot(shore_cursor, mmsi, slot)
    return len(mmsi_lst)>0

def print_db():
    db.printRows(shore_cursor)

def get_size():
    return db.get_size(shore_cursor)

# start test data
def test_data_in_db(amount):
    return db.test_data_in_db(shore_db,shore_cursor,amount)





"""

def get_top_3():  
    return db.get_top_3(shore_cursor)

def check_menu(menu):
    slot = menu[0]
    mmsi_lst = menu[1]
    # logic here
    request_lst = []
    return request_lst

"""