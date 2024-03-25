import serial
import time
import random
from collections import namedtuple

PhoneCmd = namedtuple("PhoneCmd", ["cmd", "sleep"])

APN = "web.vodafone.de"

# Define the serial port and baud rate
ser = serial.Serial("/dev/ttyS0", 115200)


# Function to send AT commands
def send_at_command(command, sleep):
    ser.write((command + "\r\n").encode())
    time.sleep(sleep)  # Wait for the response
    response = ser.read(ser.in_waiting or 1)  # Read the response from the modem
    return response.decode()


# Open serial port
if not ser.is_open:
    ser.open()

# Example AT commands
commands = [
    PhoneCmd('AT',sleep=1),
    PhoneCmd('AT+CSTT',sleep=2),
    PhoneCmd('AT+CIICR',sleep=2),
    PhoneCmd('AT+CIFSR',sleep=2),
    PhoneCmd('AT+CIPSTATUS',sleep=2),
    PhoneCmd('AT+CIPPING="google.com"',sleep=10),
    PhoneCmd('AT+CIPSHUT',sleep=1),]

# Send and print responses
for cmd, sleep in commands:
    print(f"Command: {cmd} (sleep {sleep})")
    response = send_at_command(cmd, sleep)
    print(f"Response: {response}")

# Close the serial port
ser.close()
