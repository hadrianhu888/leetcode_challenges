"""14. Longest Common Prefix
Easy
12.8K
3.8K
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters."""

def longestCommonPrefix(words):
    """Checks the longest common prefix between an array of words"""
    words_length = len(words)
    for i in range(words_length):
        for j in range(i+1, words_length):
            if words[i] == words[j]:
                return words[i]
            elif words[i] > words[j]:
                words[i] = words[i][0:len(words[j])]
            elif words[i] < words[j]:
                words[i] = words[i][0:len(words[j])]
            else:            
                words[j] = words[j][0:len(words[i])]                
    return words[0]

def main():
    """Test the function"""
    words = ["flower","flow","flight","fleeting", "flaw", "flawless", "fall"]
    print(longestCommonPrefix(words))
    
if __name__ == "__main__":
    main()  
    
# Path: longest_common_prefix.py
    


