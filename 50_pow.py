"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        power = abs(n)
        number = x
        reminder = 1
        while power > 1:
            if power % 2:
                reminder *= number
            power //= 2
            number *= number
        number *= reminder
    
        return number if n > 0 else 1 / number


if __name__ == '__main__':
    s = Solution()
    assert s.myPow(2, 10) == 1024.0
    assert round(s.myPow(2.1, 3), 5) == 9.2610, f'{round(s.myPow(2.1, 3), 5)} != 9.261'
    # assert round(s.myPow(2, -2), 5) == 0.25, f'{round(s.myPow(2, -2), 5)} != 0.25000'
    assert round(s.myPow(0.00001, 2147483647), 5) == 0.00000, f'{round(s.myPow(0.00001, 2147483647), 5)} != 0.00000'
