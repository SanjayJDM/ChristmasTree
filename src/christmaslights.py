#CHRISTMAS LIGHTS THROUGH API
#Author Sanjay JDM
from flask import Flask
from flask import json
import RPi.GPIO as GPIO
import json
import time
import urllib2
import sys

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
  except:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()
   return

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
   return
  except:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()
   return

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
   return
  except:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()
   return

def blinkCool_allTogether(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (8,10)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(chan_list, GPIO.LOW)
    time.sleep(t)
    GPIO.output(chan_list, GPIO.HIGH)
    time.sleep(t)
   GPIO.cleanup()
   return
  except:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()
   return

def blinkCool_oneAtaTime(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (8,10)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(8, GPIO.LOW)
    time.sleep(t)
    GPIO.output(8, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(10, GPIO.LOW)
    time.sleep(t)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(t)
   GPIO.cleanup()
   return
  except:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()
   return

def blinkWarm_allTogether(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (12,16)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(chan_list, GPIO.LOW)
    time.sleep(t)
    GPIO.output(chan_list, GPIO.HIGH)
    time.sleep(t)
   GPIO.cleanup()
   return
  except:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()
   return

def blinkWarm_oneAtaTime(t):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (12,16)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   while True:
    GPIO.output(12, GPIO.LOW)
    time.sleep(t)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(16, GPIO.LOW)
    time.sleep(t)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(t)
   GPIO.cleanup()
   return
  except:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()
   return

def blinkAllAtOnce(t):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)
 chan_list = (8,10,12,16)
 GPIO.setup(chan_list,GPIO.OUT)
 try:
  while True:
   GPIO.output(chan_list, GPIO.LOW)
   time.sleep(t)
   GPIO.output(chan_list, GPIO.HIGH)
   time.sleep(t)
  GPIO.cleanup()
  return
 except:
  GPIO.output(chan_list,GPIO.HIGH)
  GPIO.cleanup()
  return

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
   return
  except:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()
   return

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
   return
  except:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()
   return

def Status_allTogether(t,n):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  chan_list = (12,16)
  GPIO.setup(chan_list,GPIO.OUT)
  try:
   for x in range(n):
    GPIO.output(chan_list, GPIO.LOW)
    time.sleep(t)
    GPIO.output(chan_list, GPIO.HIGH)
    time.sleep(t)
   GPIO.cleanup()
   return
  except:
   GPIO.output(chan_list,GPIO.HIGH)
   GPIO.cleanup()
   return

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
        response=json.dumps("All Cool Lamps On"),
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
        response=json.dumps("One Cool Lamp at a time"),
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
        response=json.dumps("All Warm Lamps On"),
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
        response=json.dumps("One Walrm Lamp at a time"),
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
        response=json.dumps("Blink All"),
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
        response=json.dumps("Blink One Lamp at a time"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/random/', methods=["GET", "POST"])
def api_random():
    api_stop()
    time.sleep(0.3)
    All_differentOrder(0.3)
    response = app.response_class(
        response=json.dumps("Blink in random order"),
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
        response=json.dumps("Stay Cool Lamps ON"),
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
        response=json.dumps("Stay Warm Lamps ON"),
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
        response=json.dumps("Stay Lamps ON"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/stop/', methods=["GET", "POST"])
def api_stop():
    GPIO.cleanup()
    response = app.response_class(
        response=json.dumps("All Lamps OFF"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/kill/', methods=["GET", "POST"])
def api_kill():
    GPIO.cleanup()
    sys.exit(0)
    response = app.response_class(
        response=json.dumps("Shutdown Program"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/christmaslight/status/', methods=["GET", "POST"])
def api_status():
    GPIO.cleanup()
    request.args.get('t')
    request.args.get('n')
    response = app.response_class(
        response=json.dumps("Status of Lamps"),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
