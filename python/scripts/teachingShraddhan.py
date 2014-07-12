from urllib2 import *

proxy = {'http': 'http://172.16.1.69:3128'}

google = urlopen('http://www.google.com', proxy)

print google

# type 'python -i teachingShraddhan.py' in the terminal
