# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
#
# A shift on s consists of moving the leftmost character of s to the rightmost position.
#
# For example, if s = "abcde", then it will be "bcdea" after one shift.


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            candidate = f'{s[i:len(s) + 1]}{s[0:i]}'
            if candidate == goal:
                return True


if __name__ == '__main__':
    s = Solution()
    assert s.rotateString('abcde', 'cdeab')
    assert not s.rotateString('abcde', 'abced')
    assert s.rotateString('gcmbf', 'fgcmb')
