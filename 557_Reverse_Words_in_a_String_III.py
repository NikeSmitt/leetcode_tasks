# def reverse_words(s: str) -> str:
#     reversed_s = ''
#     left, right = 0, 0
#     white_sp_point = 0
#     for white_sp_point in range(len(s)):
#         if s[white_sp_point] == ' ':
#             right = white_sp_point - 1
#             while right >= left:
#                 reversed_s += s[right]
#                 right -= 1
#             reversed_s += s[white_sp_point]
#             left = white_sp_point + 1
#
#     right = white_sp_point
#     while right >= left:
#         reversed_s += s[right]
#         right -= 1
#
#     return reversed_s


def reverse_words(s: str) -> str:
    words = s.split()
    output = []
    for word in words:
        left, right = 0, len(word) - 1
        spam = list(word)
        while left < right:
            spam[left], spam[right] = spam[right], spam[left]
            left += 1
            right -= 1
        output.append(''.join(spam))
    return ' '.join(output)


if __name__ == "__main__":
    s = "Let's take LeetCode contest"

    result = reverse_words(s)
    expect = "s'teL ekat edoCteeL tsetnoc"
    print(result)
    print(expect == result)
