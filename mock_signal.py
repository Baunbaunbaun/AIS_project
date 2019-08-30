### NMEA MOCK SIGNAL ###

import queue
import time
import ais

# queue to hold "received" messages
NMEA_queue = queue.Queue(maxsize=1)
# settings for file operations
sleep = 0   # seconds of sleep pr row

# sample file for NMEA signals
file = open('/Users/baunbaun/dropbox/ba/BA_python/data/nmea_sample_long.txt','r') 

def setup(queue_size, sleep_input):
        global NMEA_queue
        global sleep
        NMEA_queue = queue.Queue(maxsize=queue_size)
        sleep = sleep_input
        print('MOCK setup: ', queue_size,' NMEA streaming')

        # Put [queue_size] NMEA messages in queue 
        for line in file: 
                try: 
                        if(NMEA_queue.full()):
                                break
                        NMEA_queue.put(line)
                except:
                        print('NMEA import failed with: ', line)
                        break

        print('MOCK done:', NMEA_queue.qsize(),' NMEA received')

        file.close()