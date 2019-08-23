import hashlib
import random
import time

import shore_db as sdb
import vessel_db as vdb

# import vessel

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

"""
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
vdb.vessel_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables in VDB: ", vdb.vessel_cursor.fetchall())
vdb.print_db()
# SHORE
sdb.shore_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables in SDB: ", sdb.shore_cursor.fetchall())
sdb.print_db()


# vdb.get



# vessel
#vdb_slot_5 = vdb.get_mmsi_in_slot(5)
vdb_slot_x = vdb.get_mmsi_in_slot(2)
print("VDB – get: ", vdb_slot_x)
print("VDB – send to shore 1")

# shore
#check_5 = sdb.get_mmsi_not_in_slot(vdb_slot_5)
check_x = sdb.get_mmsi_not_in_slot(vdb_slot_x)
print("SDB – what is not in slot: ", check_x)
print("SDB – send request to vessel")


# vessel
mmsi_lst = vdb.get_messages(check_x)
print("VDB – getting messages to send to shore:\n", mmsi_lst)
print("VDB – send to shore 2")


# shore
print("SDB: Receive mmsi list and insert")
sdb.insert_lst(mmsi_lst)
sdb.print_db()

"""

vdb.print_db()
sdb.print_db()







# print(top3msg)
#insert_lst(msg_test_lst)



# print(has_mmsi_in_slot(9,7))

#print(get_specific_mmsi_in_slot("(1,2,3)", 5))















host = '127.0.0.1'
port = random.randrange(1300, 65000)

for n in range(20):   
    print(random.randrange(1300, 65000))

ls = range(1)

sec1 = 10       # 1 second
sec10 = 9       # 10 seconds
sec100 = 8      # 1min 40sec (max 3 datapunkter) / 3min20 (max 6 datapunkter)
sec1000 = 7     # 16min 40sec

#print(time.time())
#print(str(time.time())[:sec100])


for i in ls:
    time.sleep(0.1)
    timestamp = str(time.time())
    hash_object = hashlib.md5(timestamp.encode())
    key = hash_object.hexdigest()
    print(i,"\t",timestamp[:sec1])

out = [1,2,3]
print(out)

out = (1,2,3)
print(out)
"""



# close DB's
vdb.db.close_db(vdb.vessel_db)
sdb.db.close_db(sdb.shore_db)

