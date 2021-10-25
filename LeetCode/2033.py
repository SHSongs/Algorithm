from typing import List

# TC: O(len(grid) * len(grid[0]))
# SC: O(len(grid) * len(grid[0]))

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sum(grid, [])
        nums.sort()

        mid = int(sum(nums) // len(nums))
        mid = min(nums, key=lambda x: abs(x - mid))  # 가장 가까운값

        res = 0

        for i in nums:
            n = abs(i - mid) / x
            # print(i, mid)
            # print(n)
            if n - int(n) == 0:
                res += abs(i - mid) / x
            else:
                return -1

        return int(res)


s = Solution()
# print(s.minOperations(grid=[[2, 4], [6, 8]], x=2))  # 4
# print(s.minOperations(grid=[[1, 5], [2, 3]], x=1))  # 5
# print(s.minOperations(grid=[[1, 2], [3, 4]], x=2))  # -1
print(s.minOperations([[980, 476, 644, 56], [644, 140, 812, 308], [812, 812, 896, 560], [728, 476, 56, 812]], 84))  # 45

# Wrong Answer