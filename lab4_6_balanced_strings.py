

s1 = input("Enter first string")
s2 = input("Enter second string")

balanced = True
for letter in s1:
    if letter not in s2:
         balanced = False
         break

if balanced:
    print("String s1 and s2 are balanced")
else:
    print("String s1 and s2 are not balanced")
