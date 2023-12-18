"""
This module provides functions for converting octal numbers to decimal, hexadecimal, and binary.
"""

decimal2hex = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'}


def octal2decimal(octal):
    decimal = 0
    for i in range(len(octal)):
        decimal += int(octal[i]) * 8 ** (len(octal) - 1 - i)
    return decimal


def octal2hex(octal):
    hex = 0
    for i in range(len(octal)):
        hex += int(octal[i]) * 16 ** (len(octal) - 1 - i)
    return hex


def dec2hex(decimal): # decimal to hex
    hex = ''
    while decimal != 0:
        hex = decimal2hex[decimal % 16] + hex
        decimal //= 16
    return hex
    
    
def dec2binary(decimal): # decimal to binary
    binary = ''
    while decimal != 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary


def main():
    octal = input('Enter an octal number: ')
    print('Decimal number is: ', octal2decimal(octal))
    print("Hexadecimal number is: ", dec2hex(octal2decimal(octal)))
    print("Binary number is: ", dec2binary(octal2decimal(octal)))


if __name__ == '__main__':
    main()
