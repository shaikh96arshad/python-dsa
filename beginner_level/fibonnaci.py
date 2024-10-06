"""
Fibonnaci series
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

"""

def fibbonaci(n):
    seq = [0,1]
    if n <= 2:
        return seq
    
    def helper(curr,n):

        print(curr,n)
        seq.append(sum(seq[-2:]))
        if n == curr:
            return 
        
        return helper(curr+1,n)
    # return 
    helper(1,n)
    return seq
    
print(fibbonaci(6))