### VESSEL DB ###
import db

# create db
vessel_db, vessel_cursor = db.create_DB('vessel')
# create table for incoming AIS
db.create_msg_table(vessel_db, vessel_cursor)

def insert(key, slot, mmsi, timestamp, x, y):
    db.insert(vessel_db, vessel_cursor, key, slot, mmsi, timestamp, x, y)

def get_mmsi_in_slot(slot):
    return db.get_mmsi_in_slot(vessel_cursor, slot) 

def get_messages(lst): # [slot, [mmsi_lst]]
    return db.get_messages(vessel_cursor, lst)

def print_db():
    db.printRows(vessel_cursor)

def get_size():
    return db.get_size(vessel_cursor)

# start test data
def test_data_in_db(amount):
    return db.test_data_in_db(vessel_db,vessel_cursor,amount)

def delete(slot):
    db.delete(vessel_db,vessel_cursor,slot)