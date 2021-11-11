from collections import deque
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        Q = deque()
        visit = set()
        Q.append((start, 0))
        visit.add(start)
        while len(Q) > 0:
            x, cnt = Q.popleft()
            for i in nums:
                for next_x in (x + i, x - i, x ^ i):
                    if next_x == goal:
                        return cnt + 1

                    if 0 <= next_x <= 1000 and next_x not in visit:
                        visit.add(next_x)
                        Q.append((next_x, cnt + 1))
        return -1


s = Solution()
print(s.minimumOperations(nums=[3, 5, 7], start=0, goal=-4))
print(s.minimumOperations(nums=[2, 8, 16], start=0, goal=1))
