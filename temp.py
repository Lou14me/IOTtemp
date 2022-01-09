import time, RPi.GPIO as GPIO
import urllib
import Adafruit_DHT as dht

def fetch_thing(url,params,method):
  params = urllib.urlencode(params)
  if method == 'POST':
    f = urllib.urlopen(url,params)
  else:
    f = urllib.urlopen(url+'?'+params)
   return (f.read(),f.code)

h,temp = dht.read_retry(dht.DHT22,4)
print 'Temp = %.1f"C,Humidity = %.1f%%RH'%(temp,h)

content,response_code = fetch_thing(
  'http://127.0.0.1/settemp.php',{'id': 1,'temp':temp},'GET'
)
