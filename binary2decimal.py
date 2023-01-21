def binary2decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal


def main():
    binary = input('Enter a binary number: ')
    print('Decimal number is: ', binary2decimal(binary))


if __name__ == '__main__':
    main()
