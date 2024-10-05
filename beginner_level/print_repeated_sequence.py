"""
print sequence like 5,4,3,2,1,1,2,3,4,5
n,n-1,n-2....1,1...n-2,n-1,n
"""
def seq(n):
    if n == 0:
        return
    else:
        print(n)
        seq(n-1)
        print(n)

# seq(5)

"""
Find sum from 0 to n
1,2,3,4,5,6..n
"""

def sum(curr,n):
    if curr == n: return curr
    else:
        return curr + sum(curr+1,n
        )
    
# print(sum(0,4))

def sum_rev(n):
    if n == 0: 
        return 0
    else:
        return n + sum_rev(n-1)
    

# print(sum_rev(4))

# print target sum indices

# def calculate_sum_index(target,array):
#     n = len(array)
#     i,j = 0,n-1
#     for k in range(n):
#         if array[i]+array[j] == target:
#             return i,j
#         else:
#             i+=1
#             j-=1

# if __name__ == '__main__':
#     print(calculate_sum_index(6,[2,4,1]))
