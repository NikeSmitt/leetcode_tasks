"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.


"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s_ = s.replace('-', '').upper()
        print(s_)
        output = []
        i = len(s_)
        while i - k > 0:
            output.append(s_[i - k: i])
            i -= k
        if i:
            output.append(s_[0:i])
        output = output[::-1]
        return '-'.join(output)
    
    
    
    
if __name__ == '__main__':
    s = Solution()
    assert s.licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"
    assert s.licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J"
