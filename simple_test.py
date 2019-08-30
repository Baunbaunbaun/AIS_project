### SIMPLE TEST PROGRAM ###

import vessel_db as vdb
import shore_db as sdb
import vessel_connection as vcon

# fill up vessel DB and shore DB LAISY messages that only 
# consists of small integers
slots_vessel = vdb.test_data_in_db(10)
print('Initial size of vessel DB: ', vdb.get_size())
slots_shore = sdb.test_data_in_db(6)

# fill up vessel send_queue
for slot in slots_vessel:
    lst = vdb.get_mmsi_in_slot(slot)
    vcon.send_queue.put(lst)

vcon.send()