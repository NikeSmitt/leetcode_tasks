# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        bank = {}
        output = 0
        for ch in s:
            count = bank.setdefault(ch, 0)
            bank[ch] = count + 1
        
        for k, v in bank.items():
            output += v // 2 * 2
            if output % 2 == 0 and v % 2 == 1:
                output += 1
        
        return output


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('abccccdd'))
    assert 7 == s.longestPalindrome('abccccdd')
    assert 1 == s.longestPalindrome('a')
