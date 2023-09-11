def binary_to_decimal(binary, expo=1):
    if binary == 0:
        return 0
    else:
        digit = binary % 10
        binary = int(binary/10)
        digit = digit*expo
        return digit + binary_to_decimal(binary, expo*2)

n = int(input("Enter binary number:"))
print(binary_to_decimal(n))


