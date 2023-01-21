def decimal2octal(decimal):
    octal = 0
    i = 1
    while decimal != 0:
        octal += (decimal % 8) * i
        decimal //= 8
        i *= 10
    return octal


def main():
    decimal = int(input('Enter a decimal number: '))
    print('Octal number is: ', decimal2octal(decimal))


if __name__ == '__main__':
    main()
