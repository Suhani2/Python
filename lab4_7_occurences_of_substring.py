s1=input("Enter string")
s2=input("Enter substring")
print("The original string is : " + s1)
print("The substring to find : " + s2)

res = [i for i in range(len(s1)) if s1.startswith(s2, i)]

print("The start indices of the substrings are : " + str(res))