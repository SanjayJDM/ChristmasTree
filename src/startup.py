#Start up Christmas Tree
#Author Sanjay JDM

import json
import time
import urllib2

url='http://192.168.0.39:3000/christmaslight/stayall/'
jsonData = urllib2.urlopen(url).read()
print  jsonData
