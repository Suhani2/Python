def factorial(n):
    factorial = 1
    for i in range(1, n):
        factorial = factorial * i
    return factorial

n = int(input("Enter the number:"))

print("The factorial is", factorial(n))