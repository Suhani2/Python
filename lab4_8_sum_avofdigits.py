s = input("Enter string:")
l=[]
for i in s:
    if(i>='0' and i<='9'):
        l.append(int(i))
print(sum(l))
print(sum(l)/len(l))