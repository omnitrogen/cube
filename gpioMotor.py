from time import sleep
import RPi.GPIO as GPIO

DIR1 = 5
STEP1 = 6
DIR2 = 7
STEP2 = 8
DIR3 = 9
STEP3 = 10
DIR4 = 11
STEP4 = 12
DIR5 = 20 
STEP5 = 21

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200   


class MotorRotation(object):
	""" control the rotation of one motor """
	def __init__(self, DIR1, STEP1, ROT):
		self.DIR1 = DIR1
		self.STEP1 = STEP1
		self.ROT = ROT
		
		GPIO.setup(self.DIR1, GPIO.OUT)
		GPIO.setup(self.STEP1, GPIO.OUT)
		GPIO.output(self.DIR1, ROT)
		
	def rotate(self, angle, signe):
		for i in range(angle
		GPIO.output(self.STEP1, GPIO.HIGH)
		


GPIO.setmode(GPIO.BCM) #
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
GPIO.output(DIR1, CW)

GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.output(DIR2, CW)

GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)
GPIO.output(DIR3, CW)

GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(STEP4, GPIO.OUT)
GPIO.output(DIR4, CW)

GPIO.setup(DIR5, GPIO.OUT)
GPIO.setup(STEP5, GPIO.OUT)
GPIO.output(DIR5, CW)

MODE = (2, 3, 4)   # Microstep Resolution GPIO Pins #
GPIO.setup(MODE, GPIO.OUT) #
'''
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
'''
GPIO.output(MODE, (1, 0 , 1)) #

step_count = SPR * 32 
delay = .005 / 32

sleep(5)
print("motor1")
for x in range(step_count):
    GPIO.output(STEP1, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP1, GPIO.LOW)
    sleep(delay)
sleep(.5)
GPIO.output(DIR1, CCW)
for x in range(step_count):
    GPIO.output(STEP1, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP1, GPIO.LOW)
    sleep(delay)


for x in range(step_count):
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)
sleep(.5)
GPIO.output(DIR2, CCW)
for x in range(step_count):
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)


for x in range(step_count):
    GPIO.output(STEP3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)
sleep(.5)
GPIO.output(DIR3, CCW)
for x in range(step_count):
    GPIO.output(STEP3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)


for x in range(step_count):
    GPIO.output(STEP4, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(delay)
sleep(.5)
GPIO.output(DIR4, CCW)
for x in range(step_count):
    GPIO.output(STEP4, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(delay)


for x in range(step_count):
    GPIO.output(STEP5, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP5, GPIO.LOW)
    sleep(delay)
sleep(.5)
GPIO.output(DIR5, CCW)
for x in range(step_count):
    GPIO.output(STEP5, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP5, GPIO.LOW)
    sleep(delay)


GPIO.cleanup()
