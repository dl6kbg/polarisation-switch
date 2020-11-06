# Polarisation Switch Control System
Control polarisation for Wimo X-Quads using an Arduino Uno and a 8-Channel Relay Module. 
Forked from Peter (2M0SQL) - https://github.com/magicbug/polarisation-switch

This code runs on my Raspberry Pi hosting a ser2net server for my Spid RAS Rotator and Cloudlog (https://github.com/magicbug/Cloudlog).
It should also run connecting the Arduino to a Linux, Mac or Windows PC with a Python enviroment (Not tested yet). It is just comfortable for my situation.

The Arduino has to run a modifed StandardFirmata. This code uses pyFirmata to control the Arduino.

Running a 8-Channel Relay Module you are able to control:

## Polarisation for two Wimo X-Quads (VHF and UHF)
* Horizontal 
* Vertical
* RHCP
* LHCP
## Two relays left for additional control, i.e a 2x2 Antenna Switch (will add that later to the code) 

# Installation

ToDo

73 Oliver DL6KBG
