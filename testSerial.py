import serial


with serial.Serial('/dev/ttyACM0', timeout=1) as ser:
	while 1:
	   serial_data = ser.read(1000)
	   print(serial_data)
	   if serial_data != b'':
		   print(serial_data)
		   text = str(input(">>> "))
		   ser.write(str.encode(text))
		   serial_data = str.encode('')
