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

def coolLight1Blink(t):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 GPIO.setup(11,GPIO.OUT)
 try:
   GPIO.output(11, GPIO.LOW)
   if t <> 0:
    for x in range(t):
     buzzer(1)
     time.sleep(1)
   GPIO.output(11,GPIO.HIGH)
 except KeyboardInterrupt:
   GPIO.output(11,GPIO.HIGH)
   GPIO.cleanup()

def coolLight1Stay(t):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 GPIO.setup(11,GPIO.OUT)
 try:
   GPIO.output(11, GPIO.LOW)
   time.sleep(t)
   GPIO.output(11,GPIO.HIGH)
 except KeyboardInterrupt:
   GPIO.output(11,GPIO.HIGH)
   GPIO.cleanup()
# testing coolLight1Blink and coolLight1Stay

def coolLight2(t = 10):
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

def warmLight1(t = 10):
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

def warmLight2(t = 1):
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


def test():
# for x in range(7):
 while True:
  coolLight1Stay(5)
  coolLight1Blink(10)



print "Good news"
test()
