import time, queue
import sys


input = '[1566730538, [227006760, 205448890, 249191000, 316013198, 366913120, 367156850, 205507490, 366950460, 205035000, 211511850, 244660667, 272016100, 205264890, 244670316, 440009390]][1566730540, [220193000, 316005239, 235055123, 413355820, 445451000, 412764890, 412454080, 211517600, 533958000, 413376760, 413955873, 413705000, 412376480, 413901565, 413439850, 412260132, 412467240]]'
print(sys.getsizeof(input))
print(sys.getsizeof(input.encode()))


"""
lst = eval(input)
print(lst[0],lst[1])




send_queue = queue.Queue(maxsize=100)
messages = []

t = b'test'
send_queue.put('hej')
out = send_queue.get()
print(len(out))
try: 
        out = send_queue.get()
except:
        pass

print(len(out))

a = [1,2,3]
b = [2]

print(set(a)^set(b))

sleep = 0.1
cut = 9
slot_size = (10**cut) * sleep 
slot_size =  slot_size / (10**11)
print(float(slot_size))


print(sleep, cut, "{:.5f}".format(int(slot_size)))

out = 0

for t in range(100):
    time.sleep(sleep)
    tid = str(time.time())

    tid = tid.replace('.','')
    print(tid)
    slot = tid[:cut]

    if (int(slot)%2 == 0 and out != slot):
        out = slot 
        print(slot) 
"""