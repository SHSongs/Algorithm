from typing import List
import collections


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = collections.defaultdict(list)
        for node, parent in enumerate(parents):  # build graph
            graph[parent].append(node)
        n = len(parents)  # total number of nodes
        d = collections.Counter() # 같은 점수를 가진 개수 기록

        def count_nodes(node):  # number of children node + self
            p, s = 1, 0  # p: product(점수), s: sum
            for child in graph[node]:  # 각 자식 탐색 (두번이 최대)
                res = count_nodes(child)  # get its nodes count
                p *= res  # take the product
                s += res  # take the sum

            p *= max(1, n - 1 - s)  # 위쪽 노드 개수 (총 개수 - 자기 자신 - 좌우 자식)
            d[p] += 1  # count the product
            return s + 1  # 자식 노드의 개수 + 1(자신)

        count_nodes(0)  # starting from root (0)
        return d[max(d.keys())]  # return max count


s = Solution()
print(s.countHighestScoreNodes(parents=[-1, 2, 0, 2, 0]))
print(s.countHighestScoreNodes(parents=[-1, 2, 0]))
