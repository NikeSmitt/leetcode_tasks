"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.


"""

class Solution:
    
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        b = bin(n)[2:]
        return b.count('1') == 1 and b[0] == '1' and len(b) % 2
    
    
    
    
    
if __name__ == '__main__':
    s = Solution()
    assert s.isPowerOfFour(16)
    assert s.isPowerOfFour(4)
    assert not s.isPowerOfFour(5)
    assert s.isPowerOfFour(1)
