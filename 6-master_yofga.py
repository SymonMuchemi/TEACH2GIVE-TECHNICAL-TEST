# 6.  Master Yoda, a renowned Jedi Master from the Star Wars universe, is known 
# for his unique way of speaking. He often reverses the order of words in his 
# sentences. For example, instead of saying "I am home" he might say "Home 
# am I" Design a function that takes a sentence as input and returns a new 
# sentence with the words reversed in the same order that Master Yoda would 
# use. 

def master_yoga(s: str):
    """Reverses the word order in sentence

    Args:
        s (str): sentence

    Returns:
        st: sentence with reversed word order
    """
    s = s.strip()
    lst = s.split()
    
    print(lst)
    
    lst.reverse()
    lst[0] = lst[0].capitalize()
    
    return  ' '.join(lst)

print(master_yoga("I am home"))
print(master_yoga("That is good"))
