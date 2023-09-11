a = input("Enter binary number")
decimal = 0
power = 1
for i in range(len(a)):
    digit = int(a[i])
    power = 2 ** i
    result = digit * power
    decimal += result

print("Decimal equivalent is",decimal)
      