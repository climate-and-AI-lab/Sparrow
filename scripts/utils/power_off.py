import RPi.GPIO as GPIO
import serial
import time

ser = serial.Serial('/dev/ttyS0',115200)
ser.flushInput()

def power_down(power_key):
        print('SIM7600X is loging off:')
        GPIO.output(power_key,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(power_key,GPIO.LOW)
        time.sleep(18)
        print('Good bye')

power_down(4)
