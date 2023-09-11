fname = input("Enter the file name: ")
try:
    fhand = open(fname)
    for line in fhand:
        line = line.rstrip()
        if (line.startswith('NIT')):
            print(line)

except:
    print("File not found")
