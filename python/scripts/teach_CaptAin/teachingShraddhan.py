from urllib2 import *

MNIT_PROXY = 'http://172.16.1.69:3128'
proxy = {'http': MNIT_PROXY}

#google = urlopen('http://www.google.com', proxy)
google = urlopen('http://www.google.com')

with open('file_object', 'wb') as f:
    f.write(str(google))

with open('html_data', 'wb') as f:
    f.write(google.read())
# type 'python -i teachingShraddhan.py' in the terminal
