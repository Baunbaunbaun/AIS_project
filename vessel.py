### VESSEL AIS SERVICE ###

# starts mock NMEA signal
import mock_signal as mock
import vessel_db as vdb
import conn_vessel as vcon
import functions as fun
import time
import ais
import hashlib
import random
from math import log

# AIS messages types with possition data
selectedMsgs = {1,2,3,18,19,27}

# data processing
aisMsg      = ''
aisLst      = []
fragments   = ''
fragmentNum = ''
payload     = ''
fillBits    = 0

# variables for Mock signal and for DB
cut         = 10     # set slot interval: 8, 9, 10, 11 = 0.001, 0.01, 0.1, 1 seconds (slot size = sleep * cut)
hash_object = hashlib.md5(b'')
key         = ''
timestamp   = ''
mmsi        = ''
x           = ''
y           = ''
slot_size   = 1

# slot and cut works together
def set_slot_size(slot_size_in_seconds):
    global slot_size
    global cut
    slot_size = slot_size_in_seconds
    cut = log(slot_size_in_seconds, 10) + 11 
    cut = int(cut)

def NMEA_import():
    t   = str(time.time())
    t   = t.replace('.','')
    slot = int(t[:cut])  

    # make sure slot is even
    if (slot%2 != 0): slot += 1
    prev_slot = slot
    
    print('VES: importing NMEA')

    # translate NMEA msg in queue to AIS
    # break, when empty queue
    while(True):
        time.sleep(mock.sleep)

        # SLOT LOGIC
        # get initial time slot
        t   = str(time.time())
        t   = t.replace('.','')
        t = int(t[:cut])  

        # get even slot number
        if (t%2 == 0 and t != slot):
            prev_slot = slot
            slot = t
            print('new slot: %d' %prev_slot)

            # get data
            mmsi_menu = vdb.get_mmsi_in_slot(prev_slot)
            # put in send queue
            vcon.send_queue.put(mmsi_menu)

        # get NMEA message from queue
        if mock.NMEA_queue.empty(): 
            print('No more NMEA messages!')
            break

        NMEA = mock.NMEA_queue.get(block=True, timeout=1)
        NMEAlst = NMEA.split(',',)
        
        # handling fragments of size 1 to 2 
        # (really need to handle fragments up to size 5)
        try:
            fragments = NMEAlst[1]
            fragmentNum = NMEAlst[2]
            fillBits = int(NMEAlst[6][0])
        except:
            continue
        # fragment 1 of 1
        if(fragments == '1'):
            payload = NMEAlst[5]
        # fragment 1 of 2
        elif(fragments == '2' and fragmentNum == '1'):
            payload = NMEAlst[5]
            continue
        # fragment 2 of 1
        elif(fragments == '2' and fragmentNum == '2'):
            payload = payload+NMEAlst[5]
        
        # decode NMEA to AIS, save as type dictionary
        try:
            aisDict = ais.decode(payload, fillBits)
        except:
            continue
        
        # fill DB with data from selected AIS message types 
        # skip incorrect MMSI
        if( len(str(aisDict['mmsi'])) == 9 and aisDict['id'] in selectedMsgs):   
            # 128bit hashing of the NMEA payload for key value
            hash_object = hashlib.md5(payload.encode())
            # fill variables
            key = hash_object.hexdigest()
            mmsi = int(aisDict['mmsi']) 
            timestamp = str(time.time())
            x = float(aisDict['x']) 
            y = float(aisDict['y']) 

            # this try statement, skips messages already in the DB
            try:
                vdb.insert(key, slot, mmsi, timestamp, x, y)
                
                # FILL UP SDB FOR TESTING
                if(mmsi%2==0): 
                    input = key, slot, mmsi, timestamp, x, y
                    #sdb.insert(input)

            except:
                continue    

    return 

# setup TEST
set_slot_size(10)
print("Slot size set to: ", slot_size)

# setup NMEA stream
mock.setup(100, 0.1)
print(" Sleep: ", mock.sleep, " cut: ", cut, 'slot size: ', slot_size)

# start NMEA stream
mock.start_stream()

# start importing NMEA
# put MMSI_menu's in send_queue
NMEA_import()

vdb.print_db()

# start sending LAISY data to shore
vcon.send()

print('VES: import finished \nSize VDB: ', vdb.get_size())