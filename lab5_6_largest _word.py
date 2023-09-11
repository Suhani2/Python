
inputFile = "lab5_1.txt"

with open(inputFile, 'r') as filedata:
 wordsList = filedata.read().split()
 longestWordLength = len(max(wordsList, key=len))

result = [textword for textword in wordsList if len(textword) == longestWordLength]
print("The following are the longest words from a text file:")
print(result)
filedata.close()