a = int(input("Enter the lower input of the range"))
b = int(input("Enter the upper input of the range"))
even_sum = 0
odd_sum = 0
for i in range(a, b):
    if i/2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print ("Sum of even numbers", even_sum)
print ("Sum of odd numbers", odd_sum)