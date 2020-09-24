"""
Given an integer,n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""


def weird(n):
    if n in range(1,100):
        if n % 2 == 1:
            return print("Weird")
        if n % 2 == 0 and n in range(2, 6) or n >= 20:
            return print("Not Weird")
        if n % 2 == 0 and n in range(6, 20):
            return print("Weird")
        else:
            return print("O numero tem que ser entre 1 e 100")


weird(3)
weird(24)