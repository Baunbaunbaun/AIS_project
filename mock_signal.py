### NMEA MOCK SIGNAL ###

import queue
import time
import ais

# sample file for NMEA signals
file = open('/Users/baunbaun/dropbox/ba/BA_python/data/nmea_sample_200.txt','r') 

# queue to hold "received" messages
NMEA_queue = queue.Queue(maxsize=100)

# settings for file operations
sleep   = 0.1   # seconds of sleep pr row

print('MOCK:',NMEA_queue.qsize(),'NMEA p.t.')
print('MOCK: Receiving NMEA ...')        

# vessel receives an NMEA message every [sleep] and put this in a queue
count = 5000
for line in file: 
        # time.sleep(sleep)
        try: 
                if(NMEA_queue.full()):
                        break
                NMEA_queue.put(line)
                # print('put')
        except:
                print('NMEA import failed with: ', line)
                break

        if(count == 1): 
                break
        count -= 1

print('MOCK:',NMEA_queue.qsize(),'NMEA received')

# !!! DO NOT CLOSE WHILE IN USE
# when file closes, the test is over
file.close()