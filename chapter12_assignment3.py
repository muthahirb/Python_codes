# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
cnt = input('Enter the count: ')
print('you have chosen the count as : ', cnt) # For my reference
count=int(cnt)
position= input('enter the position: ')
print('you have chosen the position as: ', position) # for my reference
pos=int(position)
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
vac=1
def ul(soup,pos,vac,count):
    vap=1
    tags = soup('a')
    for tag in tags:
        #print(tag.get('href', None))
        if(vap==pos):
            url =tag.get('href')
            print('Retrieving:', url)
            if(vac==count):
                print('The name is:', tag.contents[0])
            break
        else:
            vap=vap+1
    return(url)

while True:
    if vac<=count:
        url=ul(soup,pos,vac,count)
        #print('THIS is TA: ',url)
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        vac=vac+1
        #print(vac)
    else:
        #ta=url
        #print(ta)
        break
