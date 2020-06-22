# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('the entered file doesnot exsist:',fname)
    quit()

for letter in fh:
    text=letter.upper() #converts the all texts to upper case letters
    single=text.rstrip()
    print(single)         # prints all the converted letters
