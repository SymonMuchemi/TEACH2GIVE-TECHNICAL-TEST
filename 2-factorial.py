#  Write a recursive function to calculate the factorial of a number 

def factorial(n: int):
    """calculates the factorial of a number

    Args:
        n (int): the number

    Returns:
        int: the factorial of n
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(7))
print(factorial(0))
