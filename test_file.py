import hashlib
import random
import time

import shore_db as sdb
import vessel_db as vdb

import vessel


vessel.vdb.vessel_cursor.execute("SELECT slot,mmsi,COUNT(mmsi) FROM messages GROUP BY slot, mmsi HAVING COUNT(*)>1")
print("Slot / MMSI / #MMSI\n", vessel.vdb.vessel_cursor.fetchall())
# vessel.vdb.print_db()

"""

# INSERT VDB
for i in range(1,10):
    try:
        vdb.insert(str(i), str(2), i, float(i), float(i), float(i))
    except:
        continue

# INSERT SDB
for i in range(1,4):
    input = str(i+30), str(i), i, float(i), float(i), float(i)
    try:
        sdb.insert(input)
    except:
        continue

input = str(30), str(2), 30, float(30), float(30), float(30)
# input = '4a20389b217bacde77c1e58ba4440a6c', '156654618', 205507490, 1566546180.558172, 4.34772, 51.879885

sdb.insert(input)

msg_test_lst = []
for i in range(4,20):
    input = str(i), str(i), i, i, float(i), float(i)
    msg_test_lst.append(input)

top3 = [0,1,2]
top3msg = sdb.get_top_3()

print('Msg lst: ', msg_test_lst)
"""
# prep
# fill op test db
# VESSEL
vessel.vdb.vessel_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables in VDB: ", vessel.vdb.vessel_cursor.fetchall())
# vessel.vdb.print_db()
# SHORE
vessel.sdb.shore_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables in SDB: ", vessel.sdb.shore_cursor.fetchall())
# sdb.print_db()

# print('VES: import finished\nSize VDB: ', vessel.vdb.get_size(), '\nSize SDB: ', vessel.sdb.get_size())




# vessel
#vdb_slot_5 = vdb.get_mmsi_in_slot(5)
vdb_slot_x = vdb.get_mmsi_in_slot(vessel.slot)
# print("VDB – get: ", vdb_slot_x)
print("VDB – send to shore 1")


# shore
#check_5 = sdb.get_mmsi_not_in_slot(vdb_slot_5)
check_x = sdb.get_mmsi_not_in_slot(vdb_slot_x)
# print("SDB – what is not in slot: ", check_x)
print("SDB – send request to vessel")


# vessel
mmsi_lst = vdb.get_messages(check_x)
# print("VDB – getting messages to send to shore:\n", mmsi_lst)
print("VDB – send to shore 2")

"""

# shore
print("SDB: Receive mmsi list and insert")
sdb.insert_lst(mmsi_lst)
sdb.print_db()

vdb.print_db()
sdb.print_db()

"""

print(vdb.get_size(),'\n', sdb.get_size())


# close DB's
vdb.db.close_db(vdb.vessel_db)
sdb.db.close_db(sdb.shore_db)


