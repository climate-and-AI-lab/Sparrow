## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)

## Introduction
SPARROW is an IoT platform built on top of Birdnet and Birdnet-Pi that utilizes GSM capabilities to create a real-time bird-tracking network.

## Requirements
To set up SPARROW, you will need the following:
- A laptop
- An internet connection
- Raspberry Pi Zero 2W
- An SD Card
- An SD Card Reader
- A USB Microphone or Sound Card
- A GSM Shield
- A SIM card
- A Micro-USB cable
- A buck converter 12V to 5V
- A Lead-acid Battery
- A Lead-acid Battery charger
- A housing for the device
- Some wires

## Installation
Follow these steps to install SPARROW:

1. **Prepare SD Card**:
   - Install Raspberry Pi Imager from [Raspberry Pi Software](https://www.raspberrypi.com/software/).
   - Insert the SD Card into the card reader and connect it to your laptop.
   - Click on "Choose OS" then go to "Raspberry PI OS (other)" and select "Raspberry Pi OS (Legacy, 64-bit) Lite" with the Debian Bullseye port.
   - Click on "Choose Storage" and select the SD card that Sparrow will use.
   - Click the gear icon in the bottom right to open the "Advanced options" menu
   - Set the hostname to "sparrow". Now the installation will then be reachable at "http://sparrow.local" since that is the hostname that is set during this step.
   - Select "Enable SSH" and select "Use password authentication".
   - In "Set username and password." set credentials for the system.
   - Configure the system's connection to WiFi by entering the network's name (SSID) and the password used to connect to that WiFi.
   - Adjust the locale settings for your Time zone and Keyboard layout.
   - Finally, you can save the settings and click "WRITE" to write the image to the SD card. Select "YES" and enter to allow your host system (the computer you're on now) to write the SD card.

2. **Boot Up Raspberry Pi**:
   - Insert the SD card into the Raspberry Pi and connect the microphone.
   - Power on the Raspberry Pi and allow it a few minutes to boot up.

3. **Connect to Raspberry Pi**:
   - Open the terminal on a Windows laptop by searching and opening "Command Prompt".
   - Connect to the Raspberry Pi using SSH: `ssh sparrow@sparrow.local` or your configured hostname. You can paste code on the terminal using right-click on your laptop/computer.

4. **Modify System Settings**:
   - Paste the following code into the terminal and press Enter.
     ```
     bash
     sudo sed -i 's/CONF_SWAPSIZE=100/CONF_SWAPSIZE=2048/g' /etc/dphys-swapfile &&
     sudo sed -i 's/#CONF_MAXSWAP=2048/CONF_MAXSWAP=4096/g' /etc/dphys-swapfile &&
     sudo sed -i '/^exit 0/i sudo iw wlan0 set power_save off' /etc/rc.local
     ```
   - Paste `sudo raspi-config` into the terminal and press Enter. A configuration screen will open up.
   - Use the arrow keys to navigate to "Interface Options" and press enter.
   - Now navigate down to "Serial Port" and press enter.
   - To "Would you like a login shell to be accessible over serial?", navigate to and type the Enter key on "No".
   - To  "Would you like the serial port hardware to be enabled?", navigate to and type the Enter key on "Yes".
   - Navigate to and type enter on "Finish".
   - Reboot the Raspberry Pi when prompted.

5. **Run Installation Script**:
   - Reconnect to the Raspberry Pi via SSH.
   - Paste the following command into the terminal:
     ```bash
     curl -s https://raw.githubusercontent.com/madham97/SPARROW/main/newinstaller.sh | bash
     ```

6. **Finalize Installation**:
   - After installation, the system will automatically reboot. Installation can take a while.
   - Access SPARROW using the defined hostname (e.g., "http://sparrow.local").
   - Go to "Tools" and provide credentials (default username is "birdnet" with no password).
   - Open the "Select a Model" dropdown and select the "BirdNET_GLOBAL_6K_V2.4_Model_FP16" model. Set the "Species Occurence Frequency Threshold" to 0.0005.
   - Set the Longitude and Latitude for where you want to deploy the device.
   - Configure settings, including model selection, occurrence frequency threshold, location, and notification preferences.
   - In Notifications select the "Notify each new detection" option and deselect the other options.
   - Reconnect to the Raspberry Pi via SSH.
   - Paste `nano /home/sparrow/BirdNET-Pi/scripts/utils/open.py` in the terminal
   - Use the arrow keys to go to sim_pin and edit the replace the string with your sim activation pin.
   - Press Ctrl+X. It will ask to confirm changes. Press Y and then Enter.
   - Reboot the device for changes to take effect.
