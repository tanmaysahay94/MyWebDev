#Author: Tanmay Sahay
#Description: Scrapes all SMBC comics
#Date: 28 May 2014
from urllib2 import *
import re

ignore = [1275, 1587]
for i in range(1, 3373):        #look at the most recent comic on the website. it has a number, n (in the url). the second argument to range is (n+1).
    if i in ignore:
        continue
    url = 'http://www.smbc-comics.com/?id=' + str(i) + '#comic'
    imgSrc = urlopen(url)
    elements = imgSrc.read().split()
    for element in elements:
        if re.search('smbc-comics.com/comics/20[0-9]+.*[png|gif]', element):
            required = element
            break
    imgUrl = required[5:-2]
    try:                        #added the try-except branch when the 1587th comic wasn't downloading. remove the ignore list on line 7, if you may.
        img = urlopen(imgUrl)
        if i < 10:
            serialNo = '000' + str(i)
        elif i < 100:
            serialNo = '00' + str(i)
        elif i < 1000:
            serialNo = '0' + str(i)
        else:
            serialNo = str(i)
        imgName = serialNo + '.png'
        with open(imgName, 'wb') as f:
            f.write(img.read())
    except HTTPError:
        continue
