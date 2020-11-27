#New RelicAlert Bot
#Author Sanjay JDM

import RPi.GPIO as GPIO
import json
import time
import urllib2

#8 - RED
#10 - AMBER
#12 - GREEN
#16 - BUZZER

def blinkCool(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (8,10)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   for x in range(10):
    GPIO.output(chan_list, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(chan_list, GPIO.HIGH)
    time.sleep(0.3)
   GPIO.cleanup()
  except KeyboardInterrupt:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()

def blinkWarm(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (12,16)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   for x in range(10):
    GPIO.output(chan_list, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(chan_list, GPIO.HIGH)
    time.sleep(0.3)
   GPIO.cleanup()
  except KeyboardInterrupt:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()

def coolLight1Stay(t):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 GPIO.setup(32,GPIO.OUT)
 try:
   GPIO.output(32, GPIO.LOW)
   time.sleep(t)
   GPIO.output(32,GPIO.HIGH)
 except KeyboardInterrupt:
   GPIO.output(32,GPIO.HIGH)
   GPIO.cleanup()
# testing coolLight1Blink and coolLight1Stay

def blinkAll(t):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 chan_list = (18,10,12,16)
 GPIO.setup(chan_list,GPIO.OUT)
 try:
  for x in range(10):
   GPIO.output(chan_list, GPIO.LOW)
   time.sleep(0.3)
   GPIO.output(chan_list, GPIO.HIGH)
   time.sleep(0.3)
  GPIO.cleanup()
 except KeyboardInterrupt:
  GPIO.output(chan_list,GPIO.HIGH)
  GPIO.cleanup()


def coolLight2(t = 10):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 GPIO.setup(32,GPIO.OUT)
 try:
   GPIO.output(32, GPIO.LOW)
   if t == 10:
    for x in range(4):
     time.sleep(1)
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
 try:
   while True:
    coolLight1Stay(5)
    coolLight1Blink(10)
 except KeyboardInterrupt:
   GPIO.cleanup()

print "Good news testing Blink All"
blinkAll(1)
GPIO.cleanup()
blinkCool(1)
GPIO.cleanup()
blinkWarm(1)
GPIO.cleanup()
