class Solution:
    def rearrangeArray(self, nums: list) -> list:
        nums.sort()

        i = 1

        j = len(nums) - 2 if len(nums) % 2 == 0 else len(nums) - 1

        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j -= 2

        return nums


s = Solution()
print(s.rearrangeArray(nums=[1, 2, 3, 4, 5]))
print(s.rearrangeArray(nums=[6, 2, 0, 9, 7]))
print(s.rearrangeArray(nums=[0, 1, 2, 3, 4, 5]))
