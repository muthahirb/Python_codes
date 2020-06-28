import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET



url = input('Enter - ')
if len(url) < 1:
    print('enter a vaid email id')
sum=0
data = urllib.request.urlopen(url).read()

print(data.decode())
temp=data.decode()
tree = ET.fromstring(data)
#print(tree)
counts = tree.findall('.//count')
print('user count: ',len(counts))
#print(counts)
for item in counts:
    print(item)
    curr= item.text
    sum=sum+int(curr)
print(sum)
