"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d_pat = dict()
        d_let = dict()
    
        words = s.split()
        if len(pattern) != len(words):
            return False
    
        count = 1
        for l in pattern:
            if l not in d_pat:
                d_pat[l] = count
                count += 1
    
        count = 1
        for l in words:
            if l not in d_let:
                d_let[l] = count
                count += 1
    
        pattern_code = []
        letters_code = []
        for l in pattern:
            pattern_code.append(d_pat[l])
    
        for l in words:
            letters_code.append(d_let[l])
    
        return pattern_code == letters_code


if __name__ == '__main__':
    s = Solution()
    assert s.wordPattern('abba', 'dog cat cat dog')
    assert not s.wordPattern('abba', 'dog cat cat fish')
    assert not s.wordPattern('aaaa', 'dog cat cat dog')
    assert not s.wordPattern('abba', 'dog dog dog dog')
    assert s.wordPattern('a', 'a')
