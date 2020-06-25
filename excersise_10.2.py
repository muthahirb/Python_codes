name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
count=dict()
for line in handle:
    if line.startswith("From ") :
        line=line.rstrip()
        line=line.split()
        var=line[5]
        var2=var[0:2]
        #print(var2)
        count[var2]=count.get(var2,0)+1
#print(count)

for k,v in count.items():
    new=(k,v)
    lst.append(new)
    lst=sorted(lst)
#print(lst)

for key,val in lst:
    print(key,val)

#print(lst)
