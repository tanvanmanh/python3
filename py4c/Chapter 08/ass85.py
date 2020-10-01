fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print("Cannot open file", fname)

count = 0
lst = list()

for line in fh:
    line = line.rstrip()
    if line.startswith("From:"):
        words = line.split()
        email = words[1]
        lst.append(email)
        count = count + 1
        print(email)

print("There were", count, "lines in the file with From as the first word")
