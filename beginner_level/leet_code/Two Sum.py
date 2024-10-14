"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


def two_sum():

    target = 9
    arr = [2,7,11,15]
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if (i != j) and ((arr[i]+ arr[j]) == target):
                print(i,j)
                break

def two_sum_o_n():
    target = 18
    arr = [2,7,11,15]
    two_sum = {}
    for index, num in enumerate(arr):
        # print(num,index)
        complement = target - num
        if complement in two_sum:
            # return two_sum[complement]
            print(two_sum[complement],index)
        two_sum[num] = index

if __name__ == "__main__":
    two_sum_o_n()    