#Start up Christmas Tree
#Author Sanjay JDM

import json
import time
import urllib2

url='http://121.0.0.1:3000/christmaslight/stayall/'
jsonData = urllib2.urlopen(url).read()
print  jsonData
