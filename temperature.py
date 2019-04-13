#! /usr/bin/python
 
import os
import time
from RPi import GPIO
b1=17
GPIO.setmode(GPIO.BCM)
 
 
 
GPIO.setup(b1, GPIO.IN)
while True:
    val = GPIO.input(17)
    print ("temperature = " + str(val) + "°C")
   
    fichier = open("test.txt", "w")
    fichier.write(str(val) + "°C")
    fichier.close()
    time.sleep(1)
