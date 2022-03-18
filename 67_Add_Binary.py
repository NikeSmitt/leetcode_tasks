class Solution:
    def add_binary(self, a: str, b: str) -> str:
        shift = 0
        result = []
        a_i, b_i = len(a) - 1, len(b) - 1
        
        while a_i >= 0 or b_i >= 0 or shift:
            a_spam = int(a[a_i]) if a_i >= 0 else 0
            b_spam = int(b[b_i]) if b_i >= 0 else 0
            res = a_spam ^ b_spam ^ shift
            result.append(f'{res}')
            shift = (a_spam + b_spam + shift) // 2
            a_i, b_i = a_i - 1, b_i - 1
        
        return "".join(result[::-1])


if __name__ == '__main__':
    solver = Solution()
    res = solver.add_binary("11", "1")
    print(res)
    print("100" == res)
    res = solver.add_binary("1010", "1011")
    print(res)
    print("10101" == res)
