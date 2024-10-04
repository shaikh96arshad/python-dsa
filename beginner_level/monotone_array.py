# An array is monotone increasing if it's element does not decrease from left to right
# An array is monotone decreasing if it's element does not increases from right to left
# Below determine if an array is monotone
def is_monotone(array):
    n = len(array)
    if n == 0:
        return True
    elif array[0] > array[-1]:
        # decreasing
        res = check_condition(array, '>')
    else:
        # increasing
        res = check_condition(array, '<')
    return res

def check_condition(array,condition):
    for i in range(len(array)-1):
        j = i+1
        if condition == '<':
            if array[i] <= array[j]:
                pass
            else:
                return False
        else:
            if array[i] >= array[j]:
                pass
            else:
                return False
            
    return True

result = is_monotone(array=[4,3,4])
print(result)