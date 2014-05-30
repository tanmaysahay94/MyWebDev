#Author: Tanmay Sahay
#Description: Scrapes all cyanide and happiness comics
#Date: 28 May 2014

from urllib2 import *
import re

for i in range(1, 3574):        #look at the url of the first comic. it has a number, n. second argument to range is (n+1).
    url = 'http://www.explosm.net/comics/' + str(i) + '/'
    response = urlopen(url)
    elements = response.read().split()
    required = ''
    for element in elements:
        if re.search('www.explosm.net/db/files/Comics.*[png|jpg|gif]', element):
            required += element
            break
    if required:
        print i, required
        required = required[5:-1]
        try:                    #i don't have the ignore list. clearly learnt the advantage of try-except branches :P
            img = urlopen(required)
        except HTTPError:
            continue
    else:
        continue
    if i < 100:
        serial = '00' + str(i)
    elif i < 1000:
        serial = '0' + str(i)
    else:
        serial = str(i)
    imgName = serial + '_' + required[-required[::-1].index('/'):]
    with open(imgName, 'wb') as f:
        f.write(img.read())
