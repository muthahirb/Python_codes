#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
############################################################################################################################################################################################
fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From ") :
        count=count+1
        var=line.rstrip() # this is to remove the right spaces
        var1=var.split() # this is to split the whole string into list
        print(var1[1])  #as we know that the split whill be breaking the list by spaces we can see that the 2nd space holds the email address and that is what we need

print("There were", count, "lines in the file with From as the first word")
