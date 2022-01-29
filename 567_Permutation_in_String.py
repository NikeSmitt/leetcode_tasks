# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.


def check_inclusion(s1: str, s2: str) -> bool:
    # s1_map = [0] * 26
    #
    # for ch in s1:
    #     s1_map[ord(ch) - ord('a')] += 1
    #
    # for i in range(len(s2) - len(s1) + 1):
    #     s2_map = [0] * 26
    #     for ch in s2[i:i + len(s1)]:
    #         s2_map[ord(ch) - ord('a')] += 1
    #     if s1_map == s2_map:
    #         return True
    # return False


    s1_map = {}

    len_s1 = len(s1)
    for ch in s1:
        s1_map[ch] = s1_map.setdefault(ch, 0) + 1
    for i in range(len(s2) - len(s1) + 1):
        s2_map = {}
        for ch in s2[i: i + len_s1]:
            s2_map[ch] = s2_map.setdefault(ch, 0) + 1
        if s1_map == s2_map:
            return True

    return False

if __name__ == "__main__":
    assert check_inclusion('ab', 'eidbaooo')
    assert check_inclusion('a', 'ab')
    assert check_inclusion('adc', "dcda")
    assert not check_inclusion('ab', 'eidboaoo')
