"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

1221

"""


class Solution:
    def ispalindrome(self,x:int)->bool:
        y = str(x)
        print(y[::-1])
        if y[::-1] == y:
            print(True)
        else:
            print(False)
    
    def is_optimal_palindrom(self,x:int)->bool:
        def reverse_num(x):
            reverse_num = 0
            # x = abs(x)
            while x > 0:
                digit = x % 10
                reverse_num = reverse_num * 10 + digit
                x //= 10
            # print(reverse_num)
            return reverse_num
        if x == reverse_num(x):
            # return True
            print(True)
        else:
            print(False)
            
    def is_palindrome(x):
        if x < 0 or (x%10 == 0 and x!=0): return False

        rev_half = 0
        while x > rev_half:
            rev_half = rev_half * 10 + x %10
            x //=10
        return x == rev_half or x == rev_half // 10
    



        



# ob = Solution().ispalindrome(12121)
# ob = Solution().is_optimal_palindrom(121)
ob = Solution().is_palindrome(121)