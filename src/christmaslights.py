#CHRISTMAS LIGHTS THROUGH API
#Author Sanjay JDM
from flask import Flask
from flask import json
import RPi.GPIO as GPIO
import json
import time
import urllib2

#8 - cool1
#10 - cool2
#12 - warm1
#16 - warm2

app = Flask(__name__)

@app.route('/', methods=["GET"])

def stayCool_allTogether(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (8,10)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(chan_list, GPIO.LOW)
   GPIO.output(chan_list, GPIO.HIGH)
   GPIO.cleanup()
  except KeyboardInterrupt:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()

def stayWarm_allTogether(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (12,16)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(chan_list, GPIO.LOW)
   GPIO.output(chan_list, GPIO.HIGH)
   GPIO.cleanup()
  except KeyboardInterrupt:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()

def stayAll(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (8,10,12,16)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(chan_list, GPIO.LOW)
   GPIO.output(chan_list, GPIO.HIGH)
   GPIO.cleanup()
  except KeyboardInterrupt:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()

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
   while True:
    GPIO.output(chan_list, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(chan_list, GPIO.HIGH)
    time.sleep(0.3)
   GPIO.cleanup()
  except KeyboardInterrupt:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()

def blinkWarm_oneAtaTime(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (12,16)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(16, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(16, GPIO.HIGH)
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
  while True:
   GPIO.output(chan_list, GPIO.LOW)
   time.sleep(0.3)
   GPIO.output(chan_list, GPIO.HIGH)
   time.sleep(0.3)
  GPIO.cleanup()
 except KeyboardInterrupt:
  GPIO.output(chan_list,GPIO.HIGH)
  GPIO.cleanup()

def blinkAll_oneAtaTime(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (8,10,12,16)
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
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(16, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.3)
   GPIO.cleanup()
  except KeyboardInterrupt:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()

def All_differentOrder(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (8,10,12,16)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(8, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(8, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(16, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.3)
   GPIO.cleanup()
  except KeyboardInterrupt:
   GPIO.output(chan_list,GPIO.HIGH)
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
    api_stop()
    time.sleep(0.3)
    blinkCool_allTogether(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/coolone/', methods=["GET", "POST"])
def api_coolone():
    api_stop()
    time.sleep(0.3)
    blinkCool_oneAtaTime(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/warmall/', methods=["GET", "POST"])
def api_warmall():
    api_stop()
    time.sleep(0.3)
    blinkWarm_allTogether(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/warmone/', methods=["GET", "POST"])
def api_warmone():
    api_stop()
    time.sleep(0.3)
    blinkWarm_oneAtaTime(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/blinkall/', methods=["GET", "POST"])
def api_blinkall():
    api_stop()
    time.sleep(0.3)
    blinkAllAtOnce(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/blinkone/', methods=["GET", "POST"])
def api_blinkone():
    api_stop()
    time.sleep(0.3)
    blinkAll_oneAtaTime(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/all/', methods=["GET", "POST"])
def api_all():
    api_stop()
    time.sleep(0.3)
    All_differentOrder(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/staycool/', methods=["GET", "POST"])
def api_staycool():
    api_stop()
    time.sleep(0.3)
    stayCool_allTogether(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/staywarm/', methods=["GET", "POST"])
def api_staywarm():
    api_stop()
    time.sleep(0.3)
    stayWarm_allTogether(0.3)
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/stayall/', methods=["GET", "POST"])
def api_stayall():
    api_stop()
    time.sleep(0.3)
    stayAll(0.3)
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
