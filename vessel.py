### VESSEL AIS SERVICE ###

# starts mock signal
import mock_signal as mock

# import vessel_connection
import vessel_db as vdb

# for testing
import shore_db as sdb

import functions as fun

import time
import ais
import hashlib
import random


# AIS messages types with possition data
selectedMsgs = {1,2,3,18,19,27}

# data processing
aisMsg      = ''
aisLst      = []
fragments   = ''
fragmentNum = ''
payload     = ''
fillBits    = 0

# variables for DB
cut         = 9     # set slot interval: 8, 9, 10 = 1, 10, 100 (sleep * seconds) 
hash_object = hashlib.md5(b'')
key         = ''
timestamp   = ''
slot        = int(str(time.time())[:cut]) 
if (slot%2 != 0): slot += 1

slot1       = 0
mmsi        = ''
x           = ''
y           = ''

print(" Sleep: ", mock.sleep, " cut: ", cut)

# read from queue and fill in DB
# receive NMEA messages
def NMEA_import():
    print('VES: importing NMEA')

    while(True):
        # get initial time slot
        slot = int(str(time.time())[:8]) # 100 second intervals

        t = int(str(time.time())[:cut]) # intervals
        # get even slot number
        if (t%2 == 0):
            slot = t
                
        # get NMEA message from queue
        if mock.NMEA_queue.empty(): 
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
            
            print("\n", key, slot, mmsi, timestamp, x, y)

            # timestamp = str(time.time()).replace('.', '')
            #timestamp = timestamp[:10] # 100 second intervals

            # this try statement, skips messages already in the DB
            try:
                print('VES: Row inserted!')
                vdb.insert(key, slot, mmsi, timestamp, x, y)
                if(slot%3==0): 
                    input = key, slot, mmsi, timestamp, x, y
                    sdb.insert(input)
            except:
                print("VES: insert aborted! With data:\n")  #, slot, mmsi, timestamp, x, y)
                continue

            # print(aisLst)
            # print(str(aisDict))
    print('VES: import finished')
    vdb.print_db()
    sdb.print_db()

    return 


NMEA_import()



"""
# vessel to shore loop
while (True):
    
    vdb.send_menu_to_shore(slot)

    if(mock.NMEA_queue.empty()):
        break



print("NMEA queue: ", mock.NMEA_queue)

print("VDB content: ", vdb.print_db())

# test send function, list of mmsi
"""


