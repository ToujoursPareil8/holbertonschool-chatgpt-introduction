#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function calculates the factorial of a given non-negative integer
    using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the given integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the command-line argument, convert it to an integer,
# compute its factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)

