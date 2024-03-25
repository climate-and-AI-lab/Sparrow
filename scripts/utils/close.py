import serial
import time
import random
from collections import namedtuple

PhoneCmd = namedtuple("PhoneCmd", ["cmd", "sleep"])


APN = "web.vodafone.de"
url = f"http://api.thingspeak.com/update?api_key=HPDZ4040M5DOZAZE&field3=20"


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
    # Check if the module is responsive, expected value OK
#    PhoneCmd("AT", sleep=3),
    # close or turn off network connection in case it was left open, expected value OK
#    PhoneCmd("AT+CIPSHUT", sleep=3),
    #  close GPRS context bearer in case it was left open, expected value OK
#    PhoneCmd("AT+SAPBR=0,1", sleep=3),
    #  open GPRS context establish GPRS connection
#    PhoneCmd('AT+SAPBR=3,1,"CONTYPE","GPRS"', sleep=3),
    # Set the Access Point Name (APN) for the network provider
#    PhoneCmd(f'AT+SAPBR=3,1,"APN","{APN}"', sleep=3),
    # open GPRS context bearer
#    PhoneCmd("AT+SAPBR=1,1", sleep=3),
    # initiate HTTP request
#    PhoneCmd("AT+HTTPINIT", sleep=3),
    # set parameters for http session, HTTP context identifier
#    PhoneCmd('AT+HTTPPARA="CID",1', sleep=3),
    # Set the URL to be called
#    PhoneCmd(
#        f'AT+HTTPPARA="URL","{url}"',
#        sleep=10,
#    ),
    # Initiate the HTTP GET request, send http request to specified URL get is 0
#    PhoneCmd("AT+HTTPACTION=0", sleep=3),
    # ead the HTTP response, normally contains status code 200 if successful
#    PhoneCmd("AT+HTTPREAD", sleep=3),
    # Terminate the HTTP service
    PhoneCmd("AT+CIPSHUT", sleep=3),
    #    close GPRS context bearer
    PhoneCmd("AT+SAPBR=0,1", sleep=3),
]

# Send and print responses
for cmd, sleep in commands:
    print(f"Command: {cmd} (sleep {sleep})")
    response = send_at_command(cmd, sleep)
    print(f"Response: {response}")

# Close the serial port
ser.close()
