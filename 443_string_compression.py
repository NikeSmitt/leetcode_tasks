from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        l = r = 0
        output = ''
        while r < len(chars):
            output += chars[l]
            while r < len(chars) and chars[l] == chars[r]:
                r += 1
            if r - l > 1:
                output = f'{output}{r - l}'
            l = r
            
        for i in range(len(output)):
            chars[i] = output[i]
            
        
        return len(output)


if __name__ == '__main__':
    s = Solution()
    print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
    print(s.compress(["a"]))
    print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
