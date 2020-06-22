# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count= 0
spam_confidence=0


for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count=count+1
        spam_confidence = float(line[20:])+spam_confidence
    #continue


average =spam_confidence/count
print('Average spam confidence:',average)
