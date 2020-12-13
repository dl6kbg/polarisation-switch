'''

Polarisation Switching Flask application

Developed by Peter Goodhall 2M0SQL
Complete project details: https://github.com/magicbug/polarisation-switch

adapted for Arduino running Standard-Firmata by Oliver Goldenstein DL6KBG

November 2020

!!!important note for Firmata

before uploading StandardFirmata to the Arduino add the following at void setup()

----<snip>----
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
----<snip>----

This prevents switching relays on while booting.

'''

from pyfirmata import Arduino
from pyfirmata import OUTPUT
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initiate communication with Arduino
board = Arduino('/dev/pol_switch')   # /dev/ttyUSB0
print("Polarisation Switch connected ...")

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   2 : {'name' : 'D2', 'state' : 1},
   3 : {'name' : 'D3', 'state' : 1},
   4 : {'name' : 'D4', 'state' : 1},
   5 : {'name' : 'D5', 'state' : 1},
   6 : {'name' : 'D6', 'state' : 1},
   7 : {'name' : 'D7', 'state' : 1},
   8 : {'name' : 'D8', 'state' : 1},
   9 : {'name' : 'D9', 'state' : 1},
   }

vartwo = ''
message = ''

# Set each pin as an output and make it low:
for pin in pins:
   #board.digital[pin].mode = OUTPUT
   board.digital[pin].read()

@app.route("/")
def main():
   global vartwo
   global message
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = board.digital[pin].read()

   # Put the pin dictionary into the template data dictionary:

   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

@app.route("/phase/2m/<changephase>")
def changephase(changephase):
   global vartwo
   global message

   deviceName = changephase

   if changephase== "rhcp":
      board.digital[3].write(1) # turn unused relay off to save power
      board.digital[2].write(0)
      board.digital[4].write(0)
      message = "rhcp"

   if changephase == "lhcp":
      board.digital[3].write(1) # turn unused relay off to save power
      board.digital[2].write(0)
      board.digital[4].write(1)
      message = "lhcp"

   if changephase == "v":
      board.digital[4].write(1) # turn unused relay off to save power
      board.digital[2].write(1)
      board.digital[3].write(0)
      message = "v"
   # 2m Switch is at default without power at horizontal
   if changephase == "h":
      board.digital[4].write(1) # turn unused relay off to save power
      board.digital[2].write(1)
      board.digital[3].write(1)
      message = "h"

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = board.digital[pin].read()
   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins,
      'message' : message,
      'vartwo': vartwo
   }
   print templateData

   return render_template('main.html', **templateData)

@app.route("/70cm/<phase>")
def phase(phase):
   global vartwo
   global message

   deviceName = phase

   if phase== "rhcp":
      board.digital[6].write(1) # turn unused relay off to save power
      board.digital[5].write(0)
      board.digital[7].write(0)
      vartwo = "rhcp"

   if phase == "lhcp":
      board.digital[6].write(1) # turn unused relay off to save power
      board.digital[5].write(0)
      board.digital[7].write(1)
      vartwo = "lhcp"

   if phase == "v":
      board.digital[7].write(1) # turn unused relay off to save power
      board.digital[5].write(1)
      board.digital[6].write(0)
      vartwo = "v"
      # 70cm switch is by default without power at horizontal
   if phase == "h":
      board.digital[7].write(1) # turn unused relay off to save power
      board.digital[5].write(1)
      board.digital[6].write(1)
      vartwo = "h"

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = board.digital[pin].read()
   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins,
      'message' : message,
      'vartwo': vartwo
   }

   return render_template('main.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin, action):
   global vartwo
   global message

   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      board.digital[changePin].write(0)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      board.digital[changePin].write(1)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = board.digital[pin].read()
   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

@app.route("/api/status")
def api():

 return "Running"

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
