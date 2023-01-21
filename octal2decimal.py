def octal2decimal(octal):
    decimal = 0
    for i in range(len(octal)):
        decimal += int(octal[i]) * 8 ** (len(octal) - 1 - i)
    return decimal


def main():
    octal = input('Enter an octal number: ')
    print('Decimal number is: ', octal2decimal(octal))


if __name__ == '__main__':
    main()
