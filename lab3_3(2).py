conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}


def dec_to_hexa(num):
    hexadecimal = ''
    while (num > 0):
        remainder = num % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        num = num // 16

    return hexadecimal


print(dec_to_hexa(168))