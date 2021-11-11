from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i % 10 == n:
                return i
        return -1


s = Solution()
# print(s.smallestEqual(nums=[0, 1, 2]))
print(s.smallestEqual([7, 8, 3, 5, 2, 6, 3, 1, 1, 4, 5, 4, 8, 7, 2, 0, 9, 9, 0, 5, 7, 1, 6]))
