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
- A [Raspberry Pi Zero 2W with GPIO pins](https://www.amazon.de/-/en/Raspberry-Pi-Zero-Pre-soldered-Header/dp/B07BHMRTTY/ref=sr_1_2?crid=1U3G1LC4LUR6&dib=eyJ2IjoiMSJ9.pMX2Dverh1UPUvy3-CT2PKZzuYBX-4CR4bJBmL56bBucLVsqUYEk7ZrlMYYaGf_JFFmnrFMHkzKwfTKblY__W4xFpyfCZjawgP9BSZUWtwDsySv5YItG8uHHxuMr7P54V1k1MZTjzYB_x0ZNWBjF4BvD7Zmtapf2up2p2UNLB2zw_8i4FNPatmsUyrI6LHg_MqT1K2lDO7Q2NbcMQLZcZHLwOqMHktDCESRiP1p16w0.lX783ByBqBCx8nQrlAlyEu4O9ZecxZUn5FCR3FOYNDo&dib_tag=se&keywords=raspberry+pi+zero+2+w+pre+soldered&qid=1711891247&sprefix=pi+zero+solde%2Caps%2C85&sr=8-2)
- An [SD Card](https://www.amazon.de/-/en/SanDisk-microSDXC-Smartphones-Transmission-RescuePRO/dp/B09X7C7LL1/ref=sr_1_4?crid=124HPU4S2Y417&dib=eyJ2IjoiMSJ9.wURXrQCPkQt61NVEdL51J8-N3ECAKguycmbXs10l9bhzXNj1XZCaOlgmu5NIDdr5p3ooKJAMVxdaXbOqds0hjzWj100yHkivPlvi_X_is5ism5ep3ljsl7FYql8KvTWaeeUiMN_T632gZ_pDxxhfkgbQDc6DyJwO5MRH60Giadz6LGTQdykomu62XGNdrYGSqLY08ZoFQw3Wst4ZuUZcx38zIdM6GFlFDvtwmpPi6ag.cxc0erMTjSP1LYD_LT7uXGWM4qQHO5BGBiZb1hnvBcY&dib_tag=se&keywords=sd+card&qid=1711890390&sprefix=sd+ca%2Caps%2C169&sr=8-4)
- An [SD Card Reader](https://www.amazon.de/-/en/UGREEN-Reader-Adaptor-RS-MMC-Micro/dp/B01EFPX9XA/ref=sr_1_3?crid=3V5EA6XS8ACP3&dib=eyJ2IjoiMSJ9.MDfZdife2W7wlSEfvIsibhD4US3kMJsZxQCBrx6nTkP2H_EEaN9Ezp6koMOoV3Y76c5jjoFDC36xA-YByqzqKyURihmAXhpACM2fvXgdeoQedtwLvvYGpQyeJV_4yhOJYyi8J-E6OTOw2nheyPLLAaICzx1K__ioC79IMWAlRkJ28LjGOv8hvt9Y7_Z20ooErI8iZuKQmL5lDUIPA_ZNJ1a0nVBINoTYRnZc1uWeSQ0.Go3x4CpVpko6G495aVlRXzbptUcJsrYFFo90VFIOulQ&dib_tag=se&keywords=sd+card+reader+ugreen&qid=1711890472&sprefix=sd+card+reader+ugreen%2Caps%2C82&sr=8-3)
- A [USB Microphone](https://www.amazon.de/-/en/Microphone-Omnidirectional-Transformation-Windscreen-Conferencing/dp/B07SHSHW6H/ref=sr_1_9?crid=1CSGJT897IXGN&dib=eyJ2IjoiMSJ9.oCb1QrQ94nPg9bzlTRX15_VIMEE9fvXmQ2OQVWpHMOXWkCobmgE5hUH-V460AY1NCHEqLpcEXvOqq9OKVso8uZDQUVqkJz5KVqcRP3giQ1W0K3Lu9YCPflYkU16WGthXjjLHfT2sYkImObK55817qj8C5tLboJOAB9qpQ5UxE8_niyasMl_BlS5QEa3GQEMcFxgT4OgvPo8PtPoiQP1yHvRmxSe4MxDF6UTvIHxqt2GECeiyVOTA8XSQQ6GkLKErAKfLbxJs8gueP4Ni8SCGVIO465bdWjxuf6fNGrh-1jc.-nlcn5_32-7OXBoVlE2DeMw22bJOmnLrvbC_E2BQcc8&dib_tag=se&keywords=lav+mic&qid=1711890525&sprefix=lav+mic%2Caps%2C85&sr=8-9) and [Sound Card](https://www.amazon.de/-/en/UGREEN-Adapter-Computer-Speaker-Microphone/dp/B08Y8CZB2S/ref=sr_1_4?crid=I7CPT3FHMMWP&dib=eyJ2IjoiMSJ9.XxgZgGXFZTkBWZtZJmOj98yL4LApSU93x7VVjNmDQgw_sLJFfzEN4yPyErt02T5zQR_8Y3rZYtsAefh2F3qAkv7TdMM26MH2JcPdijGGQGYbwzeG_aRLaeGxb1REXlofi_-2XnFtvMKu39F5e7o1TGSPAAXkTZzXWGaoxeECWJ-mBD7JaAIyY7OWEikbBhgsBYZO84gCZL6ZmhbQuh_-NzSHYEVFcB4dkWrqL2-SlYI.tggIZ-gfYsZVIQOBToh9B5Pz2oiplt93if96rLo_nFw&dib_tag=se&keywords=ugreen+sound+card&qid=1711890567&sprefix=ugreen+sound+card%2Caps%2C84&sr=8-4)
- A [GSM Shield](https://www.amazon.de/-/en/GSM-GPRS-GNSS-HAT-Consumption/dp/B076CPX4NN/ref=sr_1_1?crid=1U9E9WKISQQ12&dib=eyJ2IjoiMSJ9.llc-fWmdswjTD0kQRWAT6L3Exq23RTbCfDnY3luVpwBS91mD2TJXXjUhN3mC7l2Yrqg04ZrpWLq9GepQG9BUQMUT-xW9GocveRO8IQIEFd-4RbU5f1j4qo2qH_CGbLan526Zj0JoF60yEWVSW5BDvrn5yWQaxL_fhECtfTZuTy58s6RMqMYU2ZHKtPXqnTS0fCLEh2n9gpQEQxkpn6sHnfto9NXRIH_FDpcd5t6yP8g.rt7B_nRt5m5k3cPHFzGBuvUMJqmQp-gy42Ei-22G1eg&dib_tag=se&keywords=gsm+shield+waveshare&qid=1711890628&sprefix=gsm+shield+waveshare%2Caps%2C72&sr=8-1)
- A SIM card
- A Micro-USB cable
- A [12V to 5V buck converter](https://www.amazon.de/-/en/Hailege-Module-Step-Down-Supply-Converter/dp/B07XFMMY1F/ref=sr_1_3?crid=2WU92RCX5ZL68&keywords=Hailege+12v+to+5v+converter&qid=1699626009&sprefix=hailege+12v+to+5v+converter%2Caps%2C158&sr=8-3)
- A [Lead-acid Battery](https://www.amazon.de/dp/B095PBF23S/ref=sspa_dk_detail_1?pd_rd_i=B07NLBVJ82&pd_rd_w=TgEZe&content-id=amzn1.sym.253e17e0-2d18-40b0-a06d-d45df1ec6e48&pf_rd_p=253e17e0-2d18-40b0-a06d-d45df1ec6e48&pf_rd_r=3GNZ9V1ZPD0FJA05T0N5&pd_rd_wg=7PWR3&pd_rd_r=813cf7a9-e997-407a-be9c-a45b6340c682&s=diy&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy&th=1)
- A [Lead-acid Battery charger](https://www.amazon.de/-/en/Trickle-Charger-Motorcycle-Vehicles-Charging/dp/B0BJVSFH2S/ref=sr_1_8?crid=3GBI1LTYU0VIY&keywords=lead%2Bacid%2Bbattery%2Bcharger%2B2A&qid=1699623775&sprefix=lead%2Bacid%2Bbattery%2Bcharger%2B2a%2Caps%2C120&sr=8-8&th=1)
- A [housing for the device](https://www.amazon.de/-/en/LogiLink-LPS223-Weatherproof-Electronic-Protection/dp/B01M00D8GP/ref=sr_1_6?crid=3M8R8937U74LK&keywords=weatherproof%2Bbox&qid=1699625237&sprefix=weatherproof%2Bbox%2Caps%2C92&sr=8-6&th=1)
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
   - Open the terminal on a Windows laptop by searching and opening "Terminal".
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
