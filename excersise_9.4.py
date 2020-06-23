#  9.4 Write a program to read through the mbox-short.txt and
#figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word
# of those lines as the person who sent the mail. The program creates
# a Python dictionary that maps the sender's mail address to a count of
# the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most
# prolific committer.
###################################################################################
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count=dict()
for line in handle:
    if line.startswith("From ") :
        var=line.rstrip() # this is to remove the right spaces
        var1=var.split() # this is to split the whole string into list
        var2=var1[1]
        #print(var2)
        count[var2]=count.get(var2,0)+1
#print(count)
word=None
val=None
for key,value in count.items():
    if val is None or val<value:
        word=key
        val=value
print(word,val)
