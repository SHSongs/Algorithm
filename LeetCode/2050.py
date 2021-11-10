import collections
from functools import lru_cache
from typing import List

# https://leetcode.com/problems/parallel-courses-iii/discuss/1548033/Python-Easy-DFS-with-Memo

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = collections.defaultdict(list)
        prv_set = set()
        for prv, nxt in relations:
            graph[nxt - 1].append(prv - 1) # 반대로 그래프를 만듬
            prv_set.add(prv - 1) # 맨 끝 작업을 제외한 노드 set

        course_not_prv = list(set(range(0, n)) - prv_set) # 마지막 작업 노드

        @lru_cache(None)
        def dfs(course):
            prevs = graph[course]
            cost = 0
            for p in prevs:
                cost = max(cost, dfs(p))
            return cost + time[course]

        return max(dfs(course) for course in course_not_prv)


s = Solution()
print(s.minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]))
# print(s.minimumTime(n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]))
