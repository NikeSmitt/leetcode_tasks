"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

"""


class Solution:
    
    def __init__(self, ver=1):
        match ver:
            case 1:
                self.isPowerOfTwo = self._is_power_of_two_ver_1
            case 2:
                self.isPowerOfTwo = self._is_power_of_two_ver_2
    
    def _is_power_of_two_ver_1(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 2 == 0:
            n = n >> 1
        if abs(n) != 1:
            return False
        return True
    
    
    def _is_power_of_two_ver_2(self, n: int) -> bool:
        if n < 1:
            return False
        return bin(n).count('1') == 1


if __name__ == '__main__':
    s = Solution(ver=2)
    assert s.isPowerOfTwo(1)
    assert s.isPowerOfTwo(16)
    assert not s.isPowerOfTwo(-16)
    assert not s.isPowerOfTwo(3)
