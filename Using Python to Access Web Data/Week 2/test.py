import re
handle = open("regex_sum_42.txt")
numlist=list()
for line in handle :
    line = line.rstrip()
    stuff = re.findall('([0-9.]+)',line)
    for element in stuff :
        try :
            num = int(element)
            numlist.append(num)
        except :
            continue
print(sum(numlist))