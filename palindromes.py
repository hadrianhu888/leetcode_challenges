"""Checks if a string or number is a palindrome."""
import re 

def is_palindrome(word): 
    """Checks if a string is a palindrome."""
    word =  re.sub(r'\W+', '', word)
    if (word == word[::-1]):
        return True
    else: 
        return False
    
print(is_palindrome("A man, a plan, a canal: Panama"))

def is_palindrome_number(number):
    """Check if a number is a palindrome."""
    # store the original number
    original_number = number
    # reverse the number
    number = str(number)[::-1]
    # convert the reversed number to an integer
    number = int(number)
    # compare the original number with the reversed number
    if (original_number == number):
        return True
    else:
        return False
    
print(is_palindrome_number(12321))

def main():
    # get the user input
    word = input('Enter a word: ')
    number= input('Enter a number: ')
    # check if the word is a palindrome
    word_palindrome = is_palindrome(word)
    number_palindrome =  is_palindrome_number(number)
    print(word_palindrome)
    print(number_palindrome)
    
if __name__ == '__main__':
    main()
    
