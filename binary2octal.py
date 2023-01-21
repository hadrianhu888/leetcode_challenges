import numpy
from numpy import pi


def binary2octal(binary):
    binary = binary[::-1]
    octal = 0
    for i in range(len(binary)):
        octal += int(binary[i]) * 2**i
    return octal


def main():
    binary = input('Enter a binary number: ')
    print('Octal number is: ', binary2octal(binary))


if __name__ == '__main__':
    main()
