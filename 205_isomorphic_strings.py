# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No
# two characters may map to the same character, but a character may map to itself.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # bank_s = {}
        # bank_t = {}
        # s_schem = ''
        # t_schem = ''
        #
        # for i in range(len(s)):
        #     a, b = s[i], t[i]
        #     code = bank_s.setdefault(a, i + 1)
        #     s_schem = f'{s_schem}{code}'
        #     code = bank_t.setdefault(b, i + 1)
        #     t_schem = f'{t_schem}{code}'
        #
        #     if s_schem != t_schem:
        #         return False
        # return True
        
        d_s = {}
        d_t = {}
        
        for i in range(len(s)):
            v_s = d_s.setdefault(s[i], t[i])
            v_t = d_t.setdefault(t[i], s[i])
            if t[i] != v_s or s[i] != v_t:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isIsomorphic('egg', 'add')
    assert s.isIsomorphic('title', 'paper')
    assert not s.isIsomorphic('foo', 'bar')
    assert not s.isIsomorphic("badc", "baba")
    print('Tested!')
