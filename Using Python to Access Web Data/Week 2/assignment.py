import re
# read the file
name = input("Enter file:")
handle = open(name)
lst = list()
# look for integers using the re.findall() looking for a regular expression of '[0-9]+'
for line in handle:
    line = line.rstrip()
    words = re.findall('([0-9]+)', line)
    for word in words:
        try:
            num = int(word)
            lst.append(num)
        except:
            continue
print(sum(lst))
