# 5.  Design a function that takes a list of integers as input. The function should 
# return True if the list contains two consecutive threes (3 next to a 3) anywhere 
# within the list. Otherwise, it should return False. For example, the function 
# should return True for [1, 3, 3] and False for [1, 3, 1, 3]

def two_threes(lst: list):
    """check to see if a string contains two consecutive 3's

    Args:
        lst (list): list of integers

    Returns:
        bool: True or False
    """
    prev = 0
    curr = 1
    
    while curr < len(lst):
        if lst[curr] == lst[prev]:
            return True
        prev += 1
        curr += 1
    return False


print(two_threes([1, 3, 3]))
print(two_threes([1, 3, 1, 3]))
print(two_threes([3, 3, 0, 9, 3, 3]))
print(two_threes([5, 3, 7, 78, 2, 3]))
