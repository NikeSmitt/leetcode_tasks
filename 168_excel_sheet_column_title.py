# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

def letters_to_num(letters):
    def f(s):
        return ord(s.upper()) - 64
    
    # print(letters + ':', end=' ')
    result = 0
    for i, letter in enumerate(letters[::-1], start=0):
        result += 26 ** i * (ord(letter.upper()) - 64)
    return result


def num_to_letter(n):
    last = n
    output = []
    while last:
        rem = last % 26
        if rem:
            output.append(chr(rem + 64))
            last //= 26
        else:
            output.append('Z')
            last = (last // 26) - 1
    return ''.join(output[::-1])


# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         def letter_num(letter):
#             return ord(letter) - 64
#         result = 0
#         for i in

if __name__ == '__main__':
    cases = ['A', 'AB', 'ZY', 'ZZ', 'ABA']
    for case in cases:
        print(f'{case=} {letters_to_num(case)=} --> {num_to_letter(letters_to_num(case))}')

