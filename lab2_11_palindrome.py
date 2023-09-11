num = int(input("Enter the number:"))
temp = num
reverse = 0
while num > 0:
    dig = num % 10
    reverse = (reverse * 10) + dig
    num = num//10
if temp == reverse:
    print("palindrome")
else:
    print("not palindrome")

