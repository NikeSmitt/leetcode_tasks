"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowels.update([v.upper() for v in vowels])
        letters = list(s)
        l, r = 0, len(letters) - 1
        
        while l < r:
            while s[l] not in vowels and l < len(letters) - 1:
                l += 1
                if l >= r:
                    break
            while s[r] not in vowels and r > -1:
                r -= 1
                if l >= r:
                    break
            if l < r:
                letters[l], letters[r] = letters[r], letters[l]
            l += 1
            r -= 1
        return ''.join(letters)
            
    
    
    
if __name__ == '__main__':
    s = Solution()
    assert s.reverseVowels('hello') == 'holle'
    assert s.reverseVowels('leetcode') == 'leotcede'
    assert s.reverseVowels('.,') == '.,'
    
