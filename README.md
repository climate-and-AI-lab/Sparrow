## Introduction
SPARROW is an IOT platform built on top of Birdnet and Birdnet-Pi that utilizes GSM capabilities to create a real-time bird tracking network.

## Requirements
* A laptop
* An internet connection
* Raspberry Pi Zero 2W
* An SD Card
* An SD Card Reader
* A USB Microphone or Sound Card
* A GSM Shield
* A SIM card
* A Micro-USB cable
* A buck converter 12V to 5V
* A Lead-acid Battery
* A housing for the device
* Some wires

## Installation
* Install Raspberry Pi Imager from https://www.raspberrypi.com/software/
* Insert the SD Card into the card reader and connect it to your laptop
* For Operating System click on "Choose OS" then go to "Raspberry PI OS (other)" and select "Raspberry Pi OS (Legacy, 64-bit) Lite" with the Debian Bullseye port
* For Storage click on "Choose Storage" and select the SD card the Sparrow will use
* Now, click the gear icon in the bottom right to open the "Advanced options" menu
* Set the hostname to "sparrow". The installation will then be reachable at "http://sparrow.local" since that is the hostname that is set during this step.
* Select "Enable SSH" and select "Use password authentication"
* In "Set username and password." set credentials for the system.
* Configure the system's connection to WiFi by entering the network's name (SSID) and the password used to connect to that WiFi.
* Adjust the locale settings for your Time zone and Keyboard layout
* Finally, you can save the settings and click "WRITE" to write the image to the SD card. Select "YES" and enter to allow your host system (the computer you're on now) to write the SD card.
* When the SD card is ready, you'll be notified that is ok to remove it from your computer.
* Put the SD card into the Raspberry Pi, connect the microphone, power it on, and allow it a few minutes to boot up. After a few minutes, you can move on to the next step.
* On the Windows laptop open the terminal by searching and opening "Command Prompt"
* Use the username and hostname from previously to connect to the Raspberry Pi. In this example, we created the sparrow user on the sparrow.local host, so the command would be ```ssh sparrow@sparrow.local```. To paste code in the terminal you can hover the mouse over it and press right-click on your mouse/trackpad.
* When warned that you are connecting to a new machine, type yes to proceed
* You will be prompted for the password that you set. After entering the password for your user, you will be able to begin the installation!
* In the terminal paste the following code and press Enter.
```
sudo sed -i 's/CONF_SWAPSIZE=100/CONF_SWAPSIZE=2048/g' /etc/dphys-swapfile &&
sudo sed -i 's/#CONF_MAXSWAP=2048/CONF_MAXSWAP=4096/g' /etc/dphys-swapfile &&
sudo sed -i '/^exit 0/i sudo iw wlan0 set power_save off' /etc/rc.local &&
sudo raspi-config
```
* A configuration screen will open up. Use the arrow keys to navigate to "Interface Options" and press enter. This will take you into a deeper menu. In this menu, use the arrow keys to navigate down to "Serial Port" and press enter. This will open up a new menu page asking the question "Would you like a login shell to be accessible over serial?", navigate to and type the Enter key on "No". It will then open up another menu page asking the question "Would you like the serial port hardware to be enabled?", navigate to and type the Enter key on "Yes". With that complete navigate to and type enter on "Finish".
* When the prompt asks you to reboot do so.
* The connection will close since the device is rebooting. After a minute reconnect to the device using ```ssh sparrow@sparrow.local``` or the appropriate ssh command for your settings.
* Paste the following command into the terminal and press Enter
  
```curl -s https://raw.githubusercontent.com/madham97/SPARROW/main/newinstaller.sh | bash```

* Then, the installation will run and may take a little while, so just be patient.
* When the installation is finished, the system will automatically reboot. When it is booted back up, you will be able to reach Sparrow using the hostname we defined. In this installation example, it is "http://sparrow.local" so go to a browser and paste "http://sparrow.local" in the URL and press Enter
* To finalize the installation go to "Tools". You'll be prompted for credentials. The default username is "birdnet" and, by default, there is no password, so leave that empty.
* Go to "Settings"
* Open the "Select a Model" dropdown and select the "BirdNET_GLOBAL_6K_V2.4_Model_FP16" model. Set the "Species Occurence Frequency Threshold" to 0.0005
* Set the Longitude and Latitude for where you want to deploy the device
* In Notification select the "Notify each new detection" option and deselect the other options
* In the terminal on your laptop reconnect to the device using the ssh command and enter ```nano /home/sparrow/BirdNET-Pi/scripts/utils/open.py```
* Use the arrow keys to go to sim_pin and edit the replace the string with your sim activation pin
* Press Ctrl+X. It will ask to confirm changes. Press Y and then Enter.
* Reboot the device
