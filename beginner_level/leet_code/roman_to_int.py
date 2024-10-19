"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50
        }
        prev_value = 0
        num = 0
        for j,i in enumerate(s):
            current_value = conv[i]
            print(prev_value,current_value)
            if prev_value < current_value and prev_value != 0:
                print("11")
                num = num - 2 * prev_value + current_value
            else:
                
                num = num + current_value
                prev_value = current_value
        print(num)


Solution().romanToInt("IV")