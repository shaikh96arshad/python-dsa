"""
Write python code to return square of a sorted array
"""
# Optimal way
def sorted_squared(array):
    n = len(array)
    i,j = 0,n-1
    res = [0]*n

    for k in reversed(range(n)):
        if array[i]**2 > array[j]**2:
            res[k] = array[i]**2
            i+= 1
        else:
            res[k] = array[j]**2
            j-=1
    return res

# another way
def sorted_squared_1(array):
    res = [0]*len(array)
    res = [i**2 for i in array]
    res.sort()
    return res


print(sorted_squared([-7,2,4,6]))
print(sorted_squared_1([-7,2,4,6]))
