# 3.  Design a function that takes a string or sequence of characters as input and 
# returns the character that appears most frequently. 
# Eg 11189 => '1' 
# hello => l

def mode_char(s: str):
    char_freq = {}
    max_val = float('-inf')
    max_key = None

    for ch in s:
        if ch in char_freq:
            char_freq[ch] += 1  
        else:
            char_freq[ch] = 1

    # get the key with the highest frequency
    for key, val in char_freq.items():
        if val > max_val:
            max_key = key
            max_val = val

    return max_key

print(mode_char("Watermelon"))
print(mode_char("hippopotamus"))
print(mode_char("Bee"))
