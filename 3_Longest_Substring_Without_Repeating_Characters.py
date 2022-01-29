# Given a string s, find the length of the longest substring without repeating characters.


# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def length_of_longest_substring(s: str) -> int:
    pool = set()
    left = right = 0
    m_len = 0

    while right < len(s):

        if s[right] not in pool:
            pool.add(s[right])
            right += 1
            m_len = max(m_len, right - left)

        else:
            pool.remove(s[left])
            left += 1

    return m_len


# TRY TO FIX OPTIMIZE THAT 



if __name__ == '__main__':
    assert (length_of_longest_substring("abcabcbb") == 3)
    assert (length_of_longest_substring("bbbbb") == 1)
    assert (length_of_longest_substring("pwwkew") == 3)
