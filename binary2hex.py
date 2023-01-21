import numpy as np
import pandas as pd


def hexmap():
    hexmap = {}
    for i in range(10):
        hexmap[str(i)] = i
    for i in range(10, 16):
        hexmap[chr(ord('A') + i - 10)] = i
    return hexmap


def binary2hex(binary):
    hexmap = hexmap()
    hex = ''
    for i in range(0, len(binary), 4):
        nibble = binary[i:i+4]
        hex += str(hexmap[nibble])
    return hex


def main():
    binary = input('Enter a binary number: ')
    print('Hexadecimal number is: ', binary2hex(binary))


if __name__ == '__main__':
    main()
