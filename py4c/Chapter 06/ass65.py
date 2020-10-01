text = "X-DSPAM-Confidence:    0.8475";

pos = text.find(" ")
try:
    number = float(text[pos:])
except Exception as e:
    quit()
print(number)
