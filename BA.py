import io
import sys
import time
#import serial
import serial.tools.list_ports

print('test')

####### AIS MOCK SIGNAL

# SOURCE: https://maker.pro/pic/tutorial/introduction-to-python-serial-ports
ports = serial.tools.list_ports.comports()
mockPort = str(ports[0]).split()[0]
serialPort = serial.Serial(port = mockPort, baudrate=38400, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

file = open('/Users/baunbaun/dropbox/ba/BA_python/nmea-sample.txt','r') 
count = 10
while(count):
    line = file.readline()
    serialPort.write(bytes(line, 'utf-8'))
    time.sleep(1)
    count -= 1
    print(line)
    
file.close()


