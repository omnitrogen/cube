import serial

with serial.Serial('/dev/ttyACM0') as ser:
	'''
	while 1:
	   serial_data1 = ser.readline()
	   print(serial_data1)
	   serial_data2 = ser.readline()
	   print(serial_data2)
	   if serial_data1 != b'' or  serial_data2 != b'':
		   text = str(input(">>> "))
		   ser.write(str.encode(text))
		   ser.flush()
	'''
	print(ser.readline())
	ser.write(b'4')
	print(ser.readline())
	ser.write(b'5')
	print(ser.readline())
	print(ser.readline())
