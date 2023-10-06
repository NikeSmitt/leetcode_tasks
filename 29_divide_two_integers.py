"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be
truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer
range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1,
and if the quotient is strictly less than -231, then return -231. """


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = True
        if (dividend < 0 and divisor < 0) or (dividend >= 0 and divisor > 0):
            neg = False
        
        ans = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        i = 1
        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                ans += 1 << i
        
        return -ans if neg else ans


if __name__ == '__main__':
    assert 3 == Solution().divide(10, 3)
    assert -2 == Solution().divide(7, -3)
    assert 0 == Solution().divide(0, 1)
    assert 1 == Solution().divide(1, 1)
    assert 2147483648 == Solution().divide(-2147483648, -1)
