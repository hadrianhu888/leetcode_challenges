"""Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters."""

"""Minimum number of operations to convert one string to another."""

def convert_string1_to_string2(string1,string2):
    """Minimum number of operations to convert one string to another."""
    # get the length of the strings
    string1_length = len(string1)
    string2_length = len(string2)
    # create a 2D array
    dp = [[0 for _ in range(string2_length + 1)] for _ in range(string1_length + 1)]
    # fill the first row
    for i in range(1, string2_length + 1):
        dp[0][i] = dp[0][i-1] + 1
    # fill the first column
    for i in range(1, string1_length + 1):
        dp[i][0] = dp[i-1][0] + 1
    # fill the rest of the 2D array
    for i in range(1, string1_length + 1):
        for j in range(1, string2_length + 1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[string1_length][string2_length]

def display_steps(string1,string2):
    """Display the conversion steps - additions,deletions"""
    string1_length = len(string1)
    string2_length = len(string2)
    dp = convert_string1_to_string2(string1,string2)
    dp = [[0 for _ in range(string2_length + 1)] for _ in range(string1_length + 1)]   
    string1_length = len(string1)
    string2_length = len(string2)
    while (string1_length > 0 and string2_length > 0):
        if string1[string1_length-1] == string2[string2_length-1]:
            string1_length -= 1
            string2_length -= 1
        elif dp[string1_length][string2_length] == dp[string1_length][string2_length-1] + 1:
            print("Add " + string2[string2_length-1])
            string2_length -= 1
        elif dp[string1_length][string2_length] == dp[string1_length-1][string2_length] + 1:
            print("Delete " + string1[string1_length-1])
            string1_length -= 1
        else:
            print("Replace " + string1[string1_length-1] + " with " + string2[string2_length-1])
            string1_length -= 1
            string2_length -= 1
    while (string2_length > 0):
        print("Add " + string2[string2_length-1])
        string2_length -= 1
    while (string1_length > 0):
        print("Delete " + string1[string1_length-1])
        string1_length -= 1
    
def display_conversion_steps(string1,string2):
    """Display the conversion steps."""
    string1_length = len(string1)
    string2_length = len(string2)
    dp = [[0 for _ in range(string2_length + 1)] for _ in range(string1_length + 1)]
    for i in range(1, string1_length + 1):
        for j in range(1, string2_length + 1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[string1_length][string2_length]

def main():
    """Test the function."""
    string1_list=["horse","intention","abc"]
    string2_list=["ros","execution","def"]
    # use a loop to test the function
    for i in range(len(string1_list)):
        print("Minimum number of operations to convert " + string1_list[i] + " to " + string2_list[i] + " is " + str(convert_string1_to_string2(string1_list[i],string2_list[i])))
        print("Conversion steps are:")
        display_steps(string1_list[i],string2_list[i])
if __name__ == "__main__":
    main()

