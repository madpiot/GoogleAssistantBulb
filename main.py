import urllib2 as u
import time
import RPi.GPIO as m

m.setmode(m.BCM)
m.setup(21,m.OUT)

while True:
 k=u.urlopen('http://orlindustries.com/olp/device_pull?device_api_key=857b706241ba59532e7da4d1e0498df4').read()
 k= k.split('<br/>')
 k=k[0]
 k=k.split(' ')
 k=k[-1] 
 print k
 #time.sleep(1)
 if k=='ON':
  m.output(21,m.LOW)
 elif k=='OFF':
  m.output(21,m.HIGH) 
