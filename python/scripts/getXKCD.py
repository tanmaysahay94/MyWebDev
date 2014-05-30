#Author: Tanmay Sahay
#Description: Scrapes all xkcd comics
#Date: 28 May 2014

#My first working script. Yay! :D

from urllib2 import *
import re

ignore = [404, 1331, 1350]
for i in range(1, 1376):        #look at the url of the first comic. it has a number in the url, n. second argument to range is (n+1).
    if i in ignore:
        continue
    url = 'http://www.xkcd.com/' + str(i) + '/'
    comicPageSource = urlopen(url)
    elements = comicPageSource.read().split()
    for element in elements:
        if re.search('src', element) and re.search('comics', element):
            requiredImgLink = element
            if i != 826:
                break
    requiredImgLink = requiredImgLink[5:-1]
    img = urlopen(requiredImgLink)  #clearly didn't know the advantage of try-except when I wrote this script :(
    index = requiredImgLink.find('comics/') + 7
    if i < 10:
        serialNo = '000' + str(i)
    elif i < 100:
        serialNo = '00' + str(i)
    elif i < 1000:
        serialNo = '0' + str(i)
    else:
        serialNo = str(i)
    fileName = serialNo + '_' + requiredImgLink[index:]
    with open(fileName, 'wb') as f:
        f.write(img.read())
    message = str(i) + ' done :)'
    print message
