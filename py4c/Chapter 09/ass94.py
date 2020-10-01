name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print("Cannot open file", name)
    quit()

emails = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        if len(words) >= 2:
            email = words[1]
            emails[email] = emails.get(email, 0) + 1

maxEmail = None
maxCount = 0
for email, count in emails.items():
    if maxEmail == None or count > maxCount:
        maxEmail = email
        maxCount = count

print(maxEmail, maxCount)
