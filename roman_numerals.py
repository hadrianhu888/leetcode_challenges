"""Converts Roman Numeral to Arabic numerals and vice-versa"""

import numpy as np
import pandas as pd
import re as re
import sys
import os 

roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman_special_cases = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
arabic_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
arabic_special_cases = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
roman_list = list(roman_dict.keys())
arabic_list = list(arabic_dict.keys())

def roman_to_arabic(roman_numeral):
    """Converts Roman numerals to Arabic numerals"""
    roman_numeral = roman_numeral.upper()
    # given any roman numeral, the sum of the values of the letters is the arabic numeral
    # except for the special cases of IV, IX, XL, XC, CD, CM
    # Take any roman numeral and split it into a list of letters
    roman_numeral_list = list(roman_numeral)
    # Create a list of the values of the letters
    roman_numeral_values = [roman_dict[letter] for letter in roman_numeral_list]
    # read from right to left and keep a running total
    equivalent_arabic_numeral = 0
    sum = 0
    for i in range(len(roman_numeral_values)-1, -1, -1):
        """Do the conversion here and consider special cases"""
        equivalent_arabic_numeral = arabic_dict[roman_numeral_values[i]]
        sum += roman_numeral_values[i]
        if roman_numeral in roman_special_cases:
            sum -= roman_special_cases[roman_numeral]
        if equivalent_arabic_numeral in arabic_special_cases:
            sum -= arabic_special_cases[equivalent_arabic_numeral]
            equivalent_arabic_numeral = arabic_dict[roman_numeral_values[-1]]
    equivalent_arabic_numeral = sum
    return equivalent_arabic_numeral    

def arabic_to_roman(arabic_digits):
    """Divide by ten and then convert each digit to the equivalent roman numeral. Keep in mind special cases like IV, IX, XL, XC, CD, CM"""
    equivalent_roman_numeral = ''
    # convert the arabic digits to a list of digits and remember the magnitude of each digit
    # modulus by 10 to get the last digit and keep each digit and their magnitude in a list
    numbers_list = [int(digit) for digit in str(arabic_digits % 10)]
    magnitudes_list = [int(digit) for digit in str(arabic_digits % 10)]
    roman_numeral = ''
    # multiply each digit by its magnitude and then convert to roman numeral
    for i in range(len(numbers_list)):
        numbers_list[i] = numbers_list[i] * magnitudes_list[i]
        roman_numeral += arabic_list[numbers_list[i]]
        arabic_special_cases[numbers_list[i]] -= magnitudes_list[i]
        # keep in mind special cases like IV, IX, XL, XC, CD, CM
        if arabic_special_cases[numbers_list[i]] in arabic_special_cases:
            equivalent_roman_numeral += arabic_special_cases[arabic_special_cases[numbers_list[i]]]
    return equivalent_roman_numeral

def main():
    """Main function"""
    # get the user input
    roman_numeral = input('Enter a roman numeral: ')
    # convert to arabic
    arabic_numeral = roman_to_arabic(roman_numeral)
    print('The arabic numeral is: ', arabic_numeral)
    # convert to roman
    roman_numeral = arabic_to_roman(arabic_numeral)
    print('The roman numeral is: ', roman_numeral)
    
if __name__ == '__main__':
    main()
    
"""
Output:
Enter a roman numeral: IX
The arabic numeral is: 4
The roman numeral is: XI
"""