import serial
import time


'''
with serial.Serial('/dev/ttyACM0', timeout=0.1) as ser:
    i = 0
    time.sleep(2)
    t = ser.readline()
    print(t.decode())
    while i < 2:
        ser.write(str.encode(input("-> ")))
        time.sleep(1)
        t = ser.readline()
        print(t.decode())
        i += 1
'''

#with serial.Serial('/dev/ttyACM0', timeout=.1) as ser:

ser = serial.Serial('/dev/ttyACM0', timeout = .1)
hook = ""
while hook != "GO":
	time.sleep(0.001)
	hook = ser.readline().decode()
print("felix est il intelligent")
ser.write(str.encode("O"))
t = ""
while t == "":
	time.sleep(0.001)
	t = ser.readline().decode()
print(t)
print("ok")
ser.close()
