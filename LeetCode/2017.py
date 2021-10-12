from typing import List


# TC: O(N^2)
# SC: O(1)


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top, bottom = grid

        n = len(grid[0])
        min_ = float("inf")
        up = sum(top)
        down = 0

        for i in range(n):
            up -= top[i]
            score = max(up, down)
            min_ = min(score, min_)
            down += bottom[i]

        return min_


s = Solution()
print(s.gridGame(grid=[[3, 3, 1], [8, 5, 2]]))
