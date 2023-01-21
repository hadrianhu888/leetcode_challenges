import numpy as np
from numpy import pi
import pandas as pd


def octal2binary(octal):
    binary = ''
    for digit in octal:
        binary += bin(int(digit))[2:].zfill(3)
    return binary


def main():
    octal = input('Enter an octal number: ')
    print('Binary number is: ', octal2binary(octal))


if __name__ == '__main__':
    main()
