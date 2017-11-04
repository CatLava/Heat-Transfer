# opening a file and searching for numbers, Coursera coursework.
import re
fhand  = open("regex_sum_43500.txt")
go = fhand.read()

lst = list()
tots = 0
f = re.findall('[0-9]+', go)
for i in f:
    i = int(i)
    tots = tots + i
print(tots)
