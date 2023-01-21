import numpy
import pandas
import scipy.stats
import os


def decimal2binary(decimal):
    binary = []
    while decimal > 0:
        binary.append(decimal % 2)
        decimal = decimal // 2
    return binary[::-1]


def main():
    decimal = int(input('Enter a decimal number: '))
    print('Binary number is: ', decimal2binary(decimal))


if __name__ == '__main__':
    main()
