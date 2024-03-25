import RPi.GPIO as GPIO
import serial
import time

ser = serial.Serial('/dev/ttyS0',115200)
ser.flushInput()


def power_on(power_key):
        print('SIM7600X is starting:')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(power_key,GPIO.OUT)
        time.sleep(0.1)
        GPIO.output(power_key,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(power_key,GPIO.LOW)
        time.sleep(20)
        ser.flushInput()
        print('SIM7600X is ready')

power_on(4)
