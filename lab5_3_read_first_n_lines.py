
inputFile = "lab5_1.txt"
N = int(input("Enter N value: "))
with open(inputFile, 'r') as filedata:
 linesList = filedata.readlines()
 print("The following are the first",N ,"lines of a text file:")

for textline in (linesList[:N]):
 print(textline, end ='')

filedata.close()