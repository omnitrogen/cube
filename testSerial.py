import serial
import time

with serial.Serial('/dev/cu.usbmodem1421', timeout=1) as ser:
    i = 0
    time.sleep(1)
    while i < 10:
        t = ser.readline()
        print(t.decode())
        ser.write(str.encode(input("-> ")))
        time.sleep(1)
        i += 1