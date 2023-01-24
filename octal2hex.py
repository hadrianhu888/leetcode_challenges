# import the necessary packages

import octal2binary 
from octal2binary import octal2binary 
from binary2hex import binary2hex

def octal2hexadecimal(octal):
	"""Convert octal number to hexadecimal number"""
	binary = ''
	binary = octal2binary(octal)
	hex = ''
	hex = binary2hex(binary)
	
def main():
	"""Test out the function"""
	octal = 0x0137
	binary = octal2hexadecimal(octal)
	
if __name__ == 'main':
	main()

	
	