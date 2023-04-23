"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        
        def get_max_common(s1, s2):
            max_pref = ''
            for i in range(len(s1)):
                if i < len(s2) and s1[i] == s2[i]:
                    max_pref = f'{max_pref}{s1[i]}'
                else:
                    break
            return max_pref
        
        for i in range(1, len(strs)):
            output = get_max_common(output, strs[i])
        return output


if __name__ == '__main__':
    s = Solution()
    # print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    # print(s.longestCommonPrefix(["c", "acc", "ccc"]))
    print(s.longestCommonPrefix(["cir","car"]))
