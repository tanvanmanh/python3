# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except Exception as e:
    print("Cannot open file", fname)

total = 0
icount = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    line = line.replace("X-DSPAM-Confidence:", "")
    sval = line.strip()
    try:
        fval = float(sval)
    except:
        continue

    icount = icount + 1
    total = total + fval

if icount == 0:
    icount = 1
    print("Average spam confidence:", total/icount)
