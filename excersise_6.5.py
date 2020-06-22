text = "X-DSPAM-Confidence:    0.8475";
st = text.find('0')
fst=float(text[st:29])
print(fst)
