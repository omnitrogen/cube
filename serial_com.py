import serial
import time


'''
with serial.Serial('/dev/ttyACM0', timeout=1) as ser:
    i = 0
    time.sleep(1)
    while i < 2:
        t = ser.readline()
        print("t:", type(t), type(t.decode()))
        print(t.decode())
        ser.write(str.encode(input("-> ")))
        time.sleep(1)
        i += 1
'''

with serial.Serial('/dev/ttyACM0', timeout=1) as ser:
			time.sleep(1)
			if ser.readline().decode() == "GO":
				print("yeah")
				ser.write(str.encode("O"))
				t = ser.readline().decode()
				while t != "O":
					t = ser.readline().decode()
					time.sleep(0.001)
				print("ok")
			print("noooope")
			
