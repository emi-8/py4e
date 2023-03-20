# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')
txt = fh.read()
txt = txt.rstrip()

print(txt.upper())
