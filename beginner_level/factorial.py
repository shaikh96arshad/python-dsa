"""
Find factorial of a number using recursion
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


def fact_1(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

print(fact_1(5))