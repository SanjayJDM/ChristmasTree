#Christmas Light
#Author Sanjay JDM and jonathan Sanjay (real author Jonathan sanjay)
from flask import Flask
from flask import json
import os
import json
import time
import urllib2

#11 - RED
#12 - AMBER
#13 - GREEN
#16 - BUZZER
app = Flask(__name__)

@app.route('/', methods=["GET"])

def api_root():
    return {
           "url": request.url
                         }

@app.route('/gitupdate/update/', methods=["GET", "POST"])
def api_update():
    os.system("sudo pkill -f christmaslights.py")
    response = app.response_class(
        response=json.dumps("GIT ACTION"),
        status=200,
        mimetype='application/json'
    )

    os.system("sudo git pull origin develop --rebase")
    print "responsed back on git update"
    os.system("sudo python christmaslights.py")
    time.sleep(10)
    stayall = urllib2.urlopen("http://192.168.0.39:3000/christmaslight/blinkall").read()


    return response
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)


import urllib.request
