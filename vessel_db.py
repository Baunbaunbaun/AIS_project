### VESSEL DB ###
import db
import random

# create db
vessel_db, vessel_cursor = db.create_DB('vessel')
# create table for incoming AIS
db.create_msg_table(vessel_db, vessel_cursor)

# simulate function that can measure 
# connectivity on board vessel
def get_connection_level():
        return random.randint(0,2)

def insert(key, slot, mmsi, timestamp, x, y):
    db.insert(vessel_db, vessel_cursor, key, slot, mmsi, timestamp, x, y)

def get_mmsi_in_slot(slot):
    lst = db.get_mmsi_in_slot(vessel_cursor, slot) 
    out = []
    out.append(slot)
    out.append(get_connection_level())
    out.append(lst[1])
    return out

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