class Solution:
    def my_sqrt(self, x: int) -> int:
        if x < 2:
            return 1
        l, m, r = 0, x // 2, x
        
        while r - l != 1:
            m = (r + l) // 2
            if m * m > x:
                r = m
            elif m * m < x:
                l = m
            else:
                return m
        return m - 1
        
        



if __name__ == '__main__':
    solver = Solution()
    print(solver.my_sqrt(2))
    print(solver.my_sqrt(4))
    print(solver.my_sqrt(9))
    print(solver.my_sqrt(10))
    