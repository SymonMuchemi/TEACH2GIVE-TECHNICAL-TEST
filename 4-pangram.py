# 4.  Design a function that determines whether a given string is a pangram. A 
# pangram is a sentence or phrase containing every letter of the alphabet at 
# least once. Punctuation and case are typically ignored. For example, the 
# string "The quick brown fox jumps over the lazy dog" is a pangram, while 
# "Hello, world!" is not.

def pangram(s: str):
    """checks if a string contains all character in the alphabet

    Args:
        s (str): the sequence of characters

    Returns:
        bool: true or false
    """
    lower_case_s = s.lower()
    chars_in_s = ""
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    for ch in lower_case_s:
        if ch in alphabets:
            chars_in_s += ch
            
    return set(alphabets) == set(chars_in_s)

print(pangram("The quick brown fox jumps over the lazy dog")) # True
print(pangram("The quick brown fox jumps over the dog")) # False
print(pangram("qwertyuioplkjhgfdsazxcvbnm")) # True
print(pangram("Hello, world!")) # False

