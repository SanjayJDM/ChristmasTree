#CHRISTMAS LIGHTS THROUGH API
#Author Sanjay JDM
from flask import Flask
from flask import json
import RPi.GPIO as GPIO
import json
import time
import urllib2

#8 - RED
#10 - AMBER
#12 - GREEN
#16 - BUZZER

app = Flask(__name__)

@app.route('/', methods=["GET"])

def blinkCool_allTogether(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (8,10)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(chan_list, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(chan_list, GPIO.HIGH)
    time.sleep(0.3)
   GPIO.cleanup()
  except KeyboardInterrupt:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()

def blinkCool_oneAtaTime(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (8,10)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(8, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(8, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.3)
   GPIO.cleanup()
  except KeyboardInterrupt:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()

def blinkWarm_allTogether(t):
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

def blinkAllAtOnce(t):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 chan_list = (8,10,12,16)
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


print "Good news testing Blink All"
#blinkAll(1)
#GPIO.cleanup()
#blinkCool_oneAtaTime(1)
#GPIO.cleanup()
#blinkWarm(1)
#GPIO.cleanup()

#API Modules
def api_root():
    return {
           "url": request.url
                         }
@app.route('/christmaslight/coolall/', methods=["GET", "POST"])
def api_coolall():
    GPIO.cleanup()
    blinkCool_allTogether(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/coolone/', methods=["GET", "POST"])
def api_coolone():
    GPIO.cleanup()
    blinkCool_oneAtaTime(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/stop/', methods=["GET", "POST"])
def api_stop():
    GPIO.cleanup()
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
