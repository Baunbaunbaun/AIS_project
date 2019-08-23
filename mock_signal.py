### NMEA MOCK SIGNAL ###

import queue
import time
import ais

# sample file for NMEA signals
file = open('/Users/baunbaun/dropbox/ba/BA_python/data/nmea_sample_200.txt','r') 

# queue to hold "received" messages
NMEA_queue = queue.Queue(maxsize=200)

# settings for file operations
sleep   = 0.01   # seconds of sleep pr row

print('MOCK: Receiving NMEA ...')

# vessel receives an NMEA message every [sleep] and put this in a queue
for line in file: 
        time.sleep(sleep)
        try: 
                NMEA_queue.put(line)
        except:
                continue

print('MOCK:',NMEA_queue.qsize(),'NMEA received')

# !!! DO NOT CLOSE WHILE IN USE
# when file closes, the test is over
file.close()

