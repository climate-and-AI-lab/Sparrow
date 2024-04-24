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
- A [Raspberry Pi Zero 2W](https://www.amazon.de/-/en/Raspberry-Pi-Zero-2-W/dp/B09KLVX4RT) with [GPIO pins](https://www.amazon.de/-/en/dp/B0BJ1WFGMN) (Soldering will be required if unsoldered version ordered)
- An [SD Card](https://www.amazon.de/-/en/SanDisk-microSDXC-Smartphones-Transmission-RescuePRO/dp/B09X7C7LL1)
- An [SD Card Reader](https://www.amazon.de/-/en/UGREEN-Reader-Adaptor-RS-MMC-Micro/dp/B01EFPX9XA)
- A [USB Microphone](https://www.amazon.de/-/en/Microphone-Omnidirectional-Transformation-Windscreen-Conferencing/dp/B07SHSHW6H) and [Sound Card](https://www.amazon.de/-/en/UGREEN-Adapter-Computer-Speaker-Microphone/dp/B08Y8CZB2S)
- A [GSM Shield](https://www.amazon.de/-/en/GSM-GPRS-GNSS-HAT-Consumption/dp/B076CPX4NN)
- A SIM card
- A Micro-USB cable
- A [12V to 5V buck converter](https://www.amazon.de/-/en/Hailege-Module-Step-Down-Supply-Converter/dp/B07XFMMY1F)
- A [Lead-acid Battery](https://www.amazon.de/dp/B095PBF23S)
- A [Lead-acid Battery charger](https://www.amazon.de/-/en/Trickle-Charger-Motorcycle-Vehicles-Charging/dp/B0BJVSFH2S)
- A [housing for the device](https://www.amazon.de/-/en/LogiLink-LPS223-Weatherproof-Electronic-Protection/dp/B01M00D8GP)
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
   - Insert the SD card into the Raspberry Pi and connect the microphone and GSM shield holding the SIM card.
   - Power on the Raspberry Pi and allow it a few minutes to boot up.

3. **Connect to Raspberry Pi**:
   - Open the terminal on a Windows laptop by searching and opening "Terminal". Ensure that the laptop is connected to the same wifi as the Raspberry Pi!
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
   - Click on "Update Settings".
   - Click on "Advanced Settings.
   - Set "Minimum Confidence" to 0.5.
   - Click on "Update Settings".
   - Reconnect to the Raspberry Pi via SSH.
   - Paste `nano /home/sparrow/BirdNET-Pi/scripts/utils/open.py` in the terminal.
   - Use the arrow keys to go to sim_pin and edit the replace the string with your sim activation pin.
   - Press Ctrl+X. It will ask to confirm changes. Press Y and then Enter.
   - Reboot the device for changes to take effect.

7. **Device Setup**:
   - Charge the lead-acid battery using the charger.
   - Connect wires from the lead-acid battery to the buck converter at the correct poles.
   - Connect the micro-usb cable from the buck converter to the Raspberry Pi.
   - House the equipment in the housing.
   - Deploy at the desired location!
  
8. **Observing results**:
   - You can see the live incoming classifications on the Thingspeak platform at the link: https://thingspeak.com/channels/2367077/
