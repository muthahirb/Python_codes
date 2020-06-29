import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    print('enter a vaid email adress')
sum=0

data = urllib.request.urlopen(url).read()


info = json.loads(data)
print('Count',len(info['comments']))

for item in info['comments']:
    #print(item)
    current_val= item['count']
    sum=current_val+sum
print('sum',sum)
