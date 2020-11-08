
![alt text](https://user-images.githubusercontent.com/34808184/98468683-e34d9900-21db-11eb-9373-c8a89108a057.jpg)

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

* Two relays left for additional control, i.e a 2x2 Antenna Switch (will add that later to the code). 

# Installation and usage

* modify StandardFirmata on Arduino IDE

On Arduino IDE go to Examples - Firmata and choose StandardFirmata.

Before uploading StandardFirmata to the Arduino add the following at void setup()

```
void setup()
{
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
  digitalWrite(4,HIGH);
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(7,HIGH);
  digitalWrite(8,HIGH);
  digitalWrite(9,HIGH);
```

This prevents switching relays on while booting.

* install flask and pyFirmata

```
pip install Flask
pip install pyfirmata
```

* Add udev rule for the Arduino

```
nano /etc/udev/rules.d/70-polarisation-switch.rules
```

add

```
#Arduino Uno - Polarisation Switch
SUBSYSTEMS=="usb",KERNEL=="ttyUSB*",ATTRS{idVendor}=="1a86",ATTRS{idProduct}=="7523",SYMLINK+="pol_switch",GROUP="dialout",MODE="0666"
```

Check, if your board has a different Vendor and Product ID. 
The switch is then available at:

```
/dev/pol_switch
```

which is the recognized by this code. See app.py for further details.

* wiring / schematic
  
  In progress.

* Usage

```
python -O app.py
```

Your application should then be available at:
```
http://yourip:5000
```

![alt text](https://user-images.githubusercontent.com/34808184/98482214-2f123980-2200-11eb-9690-1057b1e2b93e.png)


73 Oliver DL6KBG
