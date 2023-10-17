"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [w.strip() for w in s.split()]
        return len(words[-1])


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLastWord('Hello World') == 5
    assert s.lengthOfLastWord('   fly me   to   the moon  ') == 4
    assert s.lengthOfLastWord('uffy is still joyboy') == 6
