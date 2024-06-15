# 1.  Design a function that reverses the digits of an integer. For example, 50 
# should become 5 and -12 should become -21.

def reverse_integer(n: int):
    """reverses an integer

    Args:
        n (int): the integer to be reversed

    Returns:
        int: the reversed integer
    """
    if n > 0:
        return int(str(n)[::-1])
    return int(str(abs(n))[::-1]) * -1


print(reverse_integer(32))
print(reverse_integer(-98))
print(reverse_integer(204))
