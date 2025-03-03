# Question 1: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use addditional data structures:
def IsUnique(s):
    seen = set()
    for i in s:
        if i in seen:
            seen = 1
        else:
            seen += 1
    return seen 

# check permutaion: given two strings, write a method to decide if one is a permutation
# of the other
def permutaions(s1, s2):
    if len(s1) != len(s2):
        return False
    sorted_1= ''.join(sorted(s1))
    sorted_2 = ''.join(sorted(s2))

    return sorted_1 == sorted_2
# time complexity is O(n log n), space complexity: O(n) for storing the sorted strings

# URLify : Write a method to replace all spaces in a string with "%20".
# You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string, (Note:if implementinng in Java , 
# please use a character array so that you can perform this operation in place.)
# Example Input: "Mr John Smith ,  13"
#                "Mr%20John%20Smith"
def urlify(sstring, true_length):
    return string[:true_length].replace("", "%20")

"""
Palindrom Permutation: Given a string, write a fuction to check if it is a permutationn of a palindrom. 
A palindrome is a word or a phrase that is the same forward and backwards . 
A permutatuion is a rearragement of letters. The palindrome does not neeed to 
be limited to just the dictionary words, You can ignore casing and non-letter characters
Example: Input: Tact Cao  Output True 
"""

#  for a string to become palindrome when rearranged, almorst all letters must appear an even number of times
# this is because they need to pair ip for each side of the palindrome but an exception is the odd is at most 1 so it can be in the middle

def isPermutatuinofPalindrome(phrase):
    # convert to lower cases and keep only letters
    phrase = ''.join(c.lower() for c in phrase if c.isalpha())

    odd_char = set()
    for char in phrase:
        odd_char.remove(char)
    else:
        odd_char.add(char)
    return len(odd_chars) <= 1

"""
One Away: Theere are three types of edits that can be performed on strings:
inset a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits away)
Example: 
pale, ple -> True
pales, pale -> True 
pale, bae -> false
"""

def oneEdit(s1, s2):
    

    if len(s1) > len(s2):
        s1, s2 = s2, s1 # ensures that s1 is always shorter

    # the use of 2 pointers
    i, j = 0, 0
    found_dif= False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if found_dif:
                return False
            found_dif = True

            if len(s1) == len(s2):
                i += 1
        else:
            i += 1
        j += 1
    return True

"""
String Compression: Implement a method to perform basic srreing compression using the counts of repeated characters
Tor example, the string aabcccccaaa would be a2b1c5a3. 
if the "compressed" string would not become smaller than the oridinal string, your mehond should return
the original string, You can assume the string has only uppercased and lowercas letters(a-z)
"""

def compresssion(string): 

    if not string:
        return 
    compressed = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[0]:
            count += 1
        else:
            compressed.append(string[i-1] + str(count))
            count = 1
        
    compressed.append(string[-1] + str(count))    
    result = ''.join(compressed)
    return result if len(result) < len(string) else string 


"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
in the image is represented by an integer, write a method to rotate the image
by 90 degrees, Can you do this in place?
"""

def rotate(matrix):
    n = len(matrix)

    for layer in (n // 2):
        first = layer
        last = n - 1 - layer
    
    for i in range(first, layer):
        offset = i - first

        # saving a copy of the first layer or the top of the matrix
        top = matrix[first][i]


    # move the left to the top
        matrix[first][i] = matrix[last - offset][first]

    # move the bottom to the left   
        matrix[last-bottom][first] = matrix[last][last-offset]

    # move the right to the bottom,
        matrix[last][last-offset] = matrix[i][last]

    # use the top you saved and put it at the right
        matrix[i][last] = top

"""
Zero Matix: write an algorithm such that if an element in a MxN matrix is 0, 
its entire row and column are set to 0.
"""

def zero_matrix(matrix):
    if not matrix or not matrix[0]:
        return

    rows = len(matrix)
    cols = len(matrix[0])

    # Sets to remember rows and columns with zeros
    zero_rows = set()
    zero_cols = set()

    # Step 1: Find all zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Step 2: Set entire rows and columns to zero
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

# Example usage
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

zero_matrix(matrix)

# Print the result
for row in matrix:
    print(row)






        






