import re

fhand = open('regex_sum_974954.txt')
inp = fhand.read()
lst = re.findall('[0-9]+\.*[0-9]*', inp)
print(sum(int(number) for number in lst))
