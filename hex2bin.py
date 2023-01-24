import numpy 
import scipy

"""This is a simple script to convert a hex file to a binary number"""

def hexadecimal2binary(hex):
    """Convert a hex number to a binary number"""
    return bin(int(hex, 16))

if __name__ == "__main__":
    hexInput = input("Enter a hex number: ")
    print (hexadecimal2binary(str(hexInput)))
    
    