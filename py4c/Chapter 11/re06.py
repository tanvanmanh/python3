# Search for lines that have an at sign between characters
import re
import os

#
hand = open(os.path.dirname(os.path.realpath('__file__')) + '/../mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
