from typing import List


# TC: O(N^2)
# SC: O(len(nums1) + len(nums2) + len(nums3))


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        all_lst = (list(set(nums1)) + list(set(nums2)) + list(set(nums3)))
        res = set([i for i in all_lst if all_lst.count(i) >= 2])  # O(N^2)

        return list(res)


s = Solution()
print(s.twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3]))  # nums1에 같은숫자 되있는거 주의
print(s.twoOutOfThree(nums1=[3, 1], nums2=[2, 3], nums3=[1, 2]))
print(s.twoOutOfThree(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5]))

## 다른 풀이를 보면 map을 사용하는데 hash와 map에 대해 조사해야겠다.
