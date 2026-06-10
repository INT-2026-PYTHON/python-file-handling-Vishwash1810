"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""


def has_all_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word_lower = word.lower()
    return vowels.issubset(set(word_lower))


def find_words_with_all_vowels():
     # Read the sowpods.txt file
    with open('sowpods.txt', 'r') as file:
        words = file.read().splitlines()
    
    count = 0
    
    # Process each word
    for word in words:
        if has_all_vowels(word):
            print(word)
            count += 1
    
    # Print total count
    print(f"Total words with all vowels: {count}")

