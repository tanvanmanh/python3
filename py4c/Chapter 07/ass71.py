# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except Exception as e:
    print("Cannot open file", fname)
    quit()

text = fh.read()
print(text.upper().rstrip())
