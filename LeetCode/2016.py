from typing import List


# TC: O(N^2)
# SC: O(1)

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] < nums[j]:
                    ans = max(ans, nums[j] - nums[i])

        return ans


s = Solution()
print(s.maximumDifference([7, 1, 5, 4]))

# 581202553
