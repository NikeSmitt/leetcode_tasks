# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        for i in range(len(t)):
            if s_idx == len(s):
                return True
            if s[s_idx] == t[i]:
                s_idx += 1
        return s_idx == len(s)


if __name__ == '__main__':
    s = Solution()
    assert s.isSubsequence('abc', 'ahbgdc')
    assert s.isSubsequence('', '')
    assert not s.isSubsequence("axc", "ahbgdc")
    assert s.isSubsequence("", "ahbgdc")
    assert s.isSubsequence("b", "abc")
    print('Tested!')
