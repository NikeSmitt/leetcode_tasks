# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climb_stairs(self, n: int) -> int:
        stairs = [0] * (n + 1)
        stairs[0] = 1
        stairs[1] = 1
        
        for i in range(2, n + 1):
            stairs[i] = stairs[i - 1] + stairs[i - 2]
        return stairs[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.climb_stairs(4))