#Christmas Light
#Author Sanjay JDM
from flask import Flask
from flask import json
import RPi.GPIO as GPIO
import json
import time
import urllib2

#11 - RED
#12 - AMBER
#13 - GREEN
#16 - BUZZER
app = Flask(__name__)

@app.route('/', methods=["GET"])

def redLight(t = 10):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 GPIO.setup(11,GPIO.OUT)
 try:
   GPIO.output(11, GPIO.LOW)
   if t == 10:
    for x in range(7):
     buzzer(1)
     time.sleep(1)
   time.sleep(t)
   GPIO.output(11,GPIO.HIGH)
 except KeyboardInterrupt:
   GPIO.output(11,GPIO.HIGH)
   GPIO.cleanup()

def amberLight(t = 10):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 GPIO.setup(12,GPIO.OUT)
 try:
   GPIO.output(12, GPIO.LOW)
   if t == 10:
    for x in range(4):
     buzzer(1)
     time.sleep(1)
   else :
    buzzer(t)
   time.sleep(t)
   GPIO.output(12,GPIO.HIGH)
 except KeyboardInterrupt:
   GPIO.output(12,GPIO.HIGH)
   GPIO.cleanup()

def greenLight(t = 10):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 GPIO.setup(13,GPIO.OUT)
 try:
   GPIO.output(13, GPIO.LOW)
   buzzer(1)
   time.sleep(t)
   GPIO.output(13,GPIO.HIGH)
 except KeyboardInterrupt:
   GPIO.output(13,GPIO.HIGH)
   GPIO.cleanup()

def buzzer(t = 1):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 GPIO.setup(16,GPIO.OUT)
 try:
   GPIO.output(16, GPIO.LOW)
   time.sleep(t)
   GPIO.output(16,GPIO.HIGH)
 except KeyboardInterrupt:
   GPIO.output(16,GPIO.HIGH)
   GPIO.cleanup()


 redLight()

 amberLight()
 amberLight(1)
 buzzer(1)
