# e2_eye
E2 eye with Adafruit TFT Gizmo and Circuit Python.

## Description

This code was developed to turn the Adafruit TFT Gizmo with a Circuit Playground Bluefruit into an animated eye for the E2 Droid.  (from Star Wars Visions, Season 2, Episode 1, "Sith")

The part that runs on the Circuit Playground is in CircuitPython and can be found in e2/code.py

It relies on a set of .PNG files that are included here.  There is also a Python script that generates those images, found in the rendering folder.  (This python script runs on a development host.  It is not CircuitPython and doesn't run on the Playground.)

There are also folders here named hello_beep and hello_gizmo.  Those contain code.py scripts that were used to test the Circuit Playground Bluefruit before development of the e2/code.py app commenced.

## Building and Running

In order to run this you will need the right hardware and it will need to have the right software installed:
  * Adafruit Circuit Python 8.2.5 (or higher, maybe lower, IDK.)
  * The CircuitPython libraries described below
  * The code.py file from the e2 folder
  * The images folder from this repo.

### Installing CircuitPython

Adafruit provides great instructions on how to install this.  The procedure and the exact files to use may vary depending on which hardware you have.  For my setup, the CircuitPlayground Bluefruit, I went through the following steps:
  1. Update the bootloader 
  (See https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/update-bootloader)
  I found I had to use the Command Line method to get my device updated properly.

  2. Install CircuitPython
  (See https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuitpython)


### Install Libraries

The libraries should be with the CircuitPython code you downloaded to your host system in the last step.  Look in the lib subfolder where you unzipped adafruit-circuitpython-bundle-8.x-mpy-20230920.zip.

With the Circuit Playground connected to your PC, you should see a CIRCUITPY device connected as a thumb drive.  Create a "lib" folder in the root there if it doesn't already exist.  Then copy these folders from the lib folder on your host to the lib folder on the device:
    * adafruit_ble
    * adafruit_bluefruit_connect
    * adafruit_bus_device
    * adafruit_circuitplayground
    * adafruit_display_shapes
    * adafruit_display_text
    * adafruit_gizmo
    * adafruit_hid
    * adafruit_imageload

Also copy these files from the lib folder on the host to the lib folder on the device:
    * adafruit_lis3dh.mpy
    * adafruit_st7789.mpy
    * adafruit_thermistor.mpy
    * neopixel.mpy

### Copy images to the device.

In this repository, there is a folder named images with all the pre-rendered screens each in their own .PNG file.  Copy this whole folder onto the CIRCUITPY drive.  (So the CIRCUITPY drive will now have a folder named images containing those files.)

Note that every time you write new files to the CIRCUITPY device, it will restart the Python interpreter, effectively rebooting whatever script is running.

### Copy the code.py script to the device

In the e2 folder of this repository, there's a file, code.py.  Copy that to the root of the CIRCUITPY drive.

## Integrating other code

The code to display the eye is in a class called E2_Eye.  The constructor needs no parameters.  It creates the display instance and loads the first image to display.

That class also has a service() method that the main loop should call frequently.  Each time it's called, it checks the time to see if it should do anything.  When it's time to update the eye, it chooses the next image, loads it from a file and displays it on the screen.

I've found the RAM on the Circuit Playground Bluefruit can handle loading image files one at a time indefinitely.  But I have concerns that there isn't much memory remaining for other uses and if memory gets too low, the E2_Eye class may fail when it tries to load the next one.  Be careful with that.

