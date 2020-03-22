# ESP8266-Web-Control-station
This project is a web application which uses WebSocket communication protocol to communicate with ESP8266 microcontroler. This application show how to use a different modules of the ESP microcontrolers and also how to create two-way communication between server and client using WebSocet protocol. In this project has been used following modules and sensors:
* DHT22 (Temperature and humidity sensor)
* GPIO (LED controll)
* ADC (To change Servomotor angle and LED brightness)
* PWM (Controll Servomotor, LED)
* UART (Serial communication to show errors or server's IP)
* I2C (OLED SSD1306)

User by the website can controll LED or servomotor and also check current temperature, humidity and ADC value which is controlled by potentiometer. Other used technologies:
* Ajax to create asynchronous communicatios to prevent automatic updated values of temperature, humidity and ADC
* WebSocket to handle connected users
* Http to send requests and responses betwen client and server

## Getting Started
The project consist of 3 files. First of all ESP board has to be flashed with micrypython firmware. Always first running file is boot.py. This file is responsible for connecting ESP to your WiFi. All what user have to do is add correct ssid and password in boot.py. When boot.py finished its job, firmware start executing main.py. Third file SSD1306.py is a library for OLED display so it has to be also flashed into memory.  
