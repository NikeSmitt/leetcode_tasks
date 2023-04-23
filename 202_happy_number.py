"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


class Solution:
    
    def get_sum_square_digits(self, value):
        output = 0
        while value != 0:
            output += (value % 10) ** 2
            value //= 10
        return output
    
    def isHappy(self, n: int) -> bool:
        
        slow = fast = n
        while True:
            slow = self.get_sum_square_digits(slow)
            fast = self.get_sum_square_digits(fast)
            fast = self.get_sum_square_digits(fast)
            if slow == 1:
                return True
            if slow == fast:
                return False


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(2))
