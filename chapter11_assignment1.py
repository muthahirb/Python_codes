length = input('Enter the file name: ' )
if(len(length)<1):
    fname='saple_data.txt'
else:
    fname=length

handle = open(fname)
inter=list()
import re

for line in handle:
    inte = re.findall('[0-9]+',line)
    if len(inte)>0:
        l=len(inte)
        for l in inte:      # this line was added as i had a list inside a list hence made this logic so that every time i take in the integer and append them into a list
            inter.append(l) # this is to append the values

sum=0
l=len(inter)
print('The values to be summed are: ',l)
for l in inter:
    sum=sum+int(l)
print('This is the final SUM: ', sum)
