#New RelicAlert Bot
#Author Sanjay JDM

import RPi.GPIO as GPIO
import json
import time
import urllib2

#11 - RED
#12 - AMBER
#13 - GREEN
#16 - BUZZER

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
 GPIO.setup(32,GPIO.OUT)
 try:
   GPIO.output(32, GPIO.LOW)
   if t == 10:
    for x in range(4):
     buzzer(1)
     time.sleep(1)
   else :
    buzzer(t)
   time.sleep(t)
   GPIO.output(32,GPIO.HIGH)
 except KeyboardInterrupt:
   GPIO.output(32,GPIO.HIGH)
   GPIO.cleanup()

def greenLight(t = 10):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 GPIO.setup(33,GPIO.OUT)
 try:
   GPIO.output(33, GPIO.LOW)
   buzzer(1)
   time.sleep(t)
   GPIO.output(33,GPIO.HIGH)
 except KeyboardInterrupt:
   GPIO.output(33,GPIO.HIGH)
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

#BOT token xoxb-238520891088-9rB3ZGdOiqIIUcRyFwemT049&channel Slack  Channel C6THLN6K1
#url = 'https://slack.com/api/channels.history?token=xoxb-39731808647-ymi8gtBHPAnoz6jIkdvi4dqN&channel=C0YV073RV&count=1&unreads=1&latest=now'


def single():
# for x in range(7):
 while True:
  greenLight(10)
  amberLight(1)



print "Good news"

greenLight(1)
amberLight(1)
single()
