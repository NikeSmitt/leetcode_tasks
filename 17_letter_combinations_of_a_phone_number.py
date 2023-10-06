# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
# letters.
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        num_pad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        output = []
        
        def helper(n, cur, s, arr):
            if len(s) == n:
                arr.append(s)
            else:
                for j in num_pad[digits[cur]]:
                    s = f'{s}{j}'
                    helper(n, cur + 1, s, arr)
                    s = s[:-1]
                    
        helper(len(digits), 0, '', output)
        return output

if __name__ == '__main__':
    s = Solution()
    assert ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"] == s.letterCombinations('23')
    assert ["a", "b", "c"] == s.letterCombinations('2')
    assert [] == s.letterCombinations('')
