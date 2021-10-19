from typing import List


# TC: O(n)
# SC: O(miss_total // n)

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        m = len(rolls)
        miss_total = (mean * (m + n)) - sum(rolls)
        print(miss_total)

        if n * 1 > miss_total or n * 6 < miss_total:
            return []

        x = miss_total // n

        r = miss_total - (n * x)
        print(r)

        res = [x] * (n - r) + [x + 1] * r

        return res


s = Solution()
# print(s.missingRolls(rolls=[1, 2, 3, 4], mean=6, n=4))
# print(s.missingRolls(rolls=[1], mean=3, n=1))
# print(s.missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2))
# print(s.missingRolls(rolls=[1, 5, 6], mean=3, n=4))
print(s.missingRolls([4, 5, 6, 2, 3, 6, 5, 4, 6, 4, 5, 1, 6, 3, 1, 4, 5, 5, 3, 2, 3, 5, 3, 2, 1, 5, 4, 3, 5, 1, 5]
                     , 4
                     , 40))
