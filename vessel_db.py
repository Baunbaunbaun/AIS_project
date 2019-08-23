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

# maybe just a loop in vessel?
def send_menu_to_shore():
    slot = 0
    lst = get_mmsi_in_slot(slot)
    # put in send queue

# MAX ANTAL X SAMME MMSI I SLOT?
# 100 SEKUNDER, 4 STK ?