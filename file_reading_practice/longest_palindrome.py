"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""


def is_palindrome(word):
    word_lower = word.lower()
    return word_lower == word_lower[::-1]


def find_longest_palindrome():
    with open('sowpods.txt', 'r') as file:
        words = file.read().splitlines()
    
    max_length = 0
    longest_palindromes = []
    
    for word in words:
        if is_palindrome(word):
            word_length = len(word)
            if word_length > max_length:
                max_length = word_length
                longest_palindromes = [word]
            elif word_length == max_length:
                longest_palindromes.append(word)
    
    # Print results
    print(f"Longest palindrome length: {max_length}")
    for word in longest_palindromes:
        print(word)
    
    return longest_palindromes

