fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    var=line.rstrip()
    var1=var.split()
    for w in var1:
        if w not in lst:
            lst.append(w)
lst.sort()
print(lst)
