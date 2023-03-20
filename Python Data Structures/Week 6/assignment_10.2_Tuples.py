name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()

    if len(words) < 4 or words[0] != 'From':
        continue
    word = words[5]
    for num in word:
        num = word.split(':')
    hour = num[0]
    counts[hour] = counts.get(hour, 0) + 1

lst = list()
lst = sorted([(k,v) for k,v in counts.items()])

for k,v in lst:
    print(k,v)