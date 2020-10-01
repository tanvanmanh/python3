name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print("Cannot open file", name)
    quit()

hours = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        if len(words) >= 6:
            time = words[5]
            hour, minute, second = time.split(":")
            hours[hour] = hours.get(hour, 0) + 1

hrslist = list()
for hour, count in hours.items():
    hrslist.append((hour, count))

hrslist.sort()
for item in hrslist:
    print(item[0], item[1])
