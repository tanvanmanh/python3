# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
import re
hand = open('C:\\Users\\manhtv3\\OneDrive\\Desktop\\py4c\\mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)
