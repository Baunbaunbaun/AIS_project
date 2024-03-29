import vessel_db as vdb
import shore_db as sdb
import vessel_connection as vcon

# fill up db
slots_vessel = vdb.test_data_in_db(10)
slots_shore = sdb.test_data_in_db(6)

# fill up send_queue
for slot in slots_vessel:
    lst = vdb.get_mmsi_in_slot(slot)
    vcon.send_queue.put(lst)

vcon.send()