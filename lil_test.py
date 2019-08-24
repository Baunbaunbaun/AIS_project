import time


a = [1,2,3]
b = [2]

print(set(a)^set(b))

sleep = 0.1
cut = 9
slot_size = (10**cut) * sleep 
slot_size =  slot_size / (10**11)
print(float(slot_size))

"""

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