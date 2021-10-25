from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sum(grid, [])
        nums.sort()

        m1 = nums[0] % x  # 제일 작은 수가 x를 n번 더해 중앙까지 올라와야함
        for i in nums:
            if i % x != m1:
                return -1

        median = nums[len(nums) // 2]

        res = 0

        for i in nums:
            res += abs(i - median) // x

        return res


s = Solution()
print(s.minOperations(grid=[[2, 4], [6, 8]], x=2))  # 4
print(s.minOperations(grid=[[1, 5], [2, 3]], x=1))  # 5
print(s.minOperations(grid=[[1, 2], [3, 4]], x=2))  # -1
print(s.minOperations([[980, 476, 644, 56], [644, 140, 812, 308], [812, 812, 896, 560], [728, 476, 56, 812]], 84))  # 45


# Time Limit Exceeded