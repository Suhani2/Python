str1 = "SU312NI"
print("The given string is:")

print(str1)

print("Removing all the characters except digits")
print(''.join(i for i in str1 if i.isdigit()))