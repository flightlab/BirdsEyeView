Authors (@[Altshuler Lab](https://altshuler.zoology.ubc.ca/), UBC):   
[Bhaskar Yechuri](bhaskar.yechuri@gmail.com) - Engineering Technician & Research Assistant,   
[Nick Tochor](flighttech@zoology.ubc.ca) - Lab Manager & Research Assistant,   
[Doug Altshuler](doug@zoology.ubc.ca) - Principal Investigator

# Birds-Eye-View Project

## Summary
The purpose of this project is to create lightweight cameras systems mounted on avian test subjects to better study the visual stimuli and optic flow experienced by birds during flight.

This repository contains the key information about the prototypes under development at the Flight Lab which pertain to this project. This repo also contains instructions on how to build and use the prototypes.

## Prototypes Currently in Development
Currently, there are two prototypes in use, both powered by lightweight and low-volume Lithium Polymer batteries. A summary of the two prototypes is listed below, and details, instructions can be found in each of the two folders of the same names (_PiZeroCam_ & _KeychainCam_):

* **PiZeroCam**: Based on the [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/) and a [Pi Zero Spy Cam](https://www.adafruit.com/product/3508). In addition to these parts, a couple of extenders were used to increase distance between the Pi Zero and the camera lens. There was also a startup script written in Python to begin recording video the moment it is powered, up to a maximum value pre-decided by the user. Due to the weight of this protoype (~20g), its usage is limited to birds heavier than ~130g (e.g. pigeons).
* **KeychainCam**: Built around the standalone [Spy Camera Module](https://www.adafruit.com/product/3202) sold by Adafruit. This device was modified by replacing leads with ultra-thin and flexible wiring and desoldering the mic and usb port to minimize weight/volume. This device is just light enough (~3-3.5g) to be used on medium/large zebra finches (~20g and heavier).
