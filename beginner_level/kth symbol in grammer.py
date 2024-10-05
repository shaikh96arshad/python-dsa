"""
We build a table of n rows (1-indexed).
We start by writing 0 in 1st row.
Now in every subsequent row, we look at the previous row and replace occurance of 0 with 01
and each occurance of 1 with 10. For example, for n =3
0
01
0110

For n =4
0
01
0110
01101001

Given 2 integers n & k return the kth(1-indexed) symbol in the nth row of a table of n rows
"""

def kth_symbol(n,k):
    if n == 1: return 0
    length = 2**(n-1)
    mid = length//2

    if k<= mid:
        return kth_symbol(n-1,k)
    else:
        return int(not(kth_symbol(n-1,k-mid)))



if __name__ == "__main__":
    print(kth_symbol(3,1))
    print(kth_symbol(4,5))