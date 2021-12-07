from typing import List
# 동작하지 않음

class Solution:
    def minimumOperations(self, plants: List[int], capacity: int) -> int:
        now_capacity = capacity
        step_cnt = 0

        for i in range(len(plants)):
            recharging = False
            if now_capacity <= 0 or plants[i] > now_capacity:
                now_capacity = capacity
                step_cnt += i
                recharging = True

            if plants[i] - now_capacity <= 0:  # 물 주기
                now_capacity -= plants[i]
                if recharging:
                    step_cnt += i + 2
                else:
                    step_cnt += 1


        return step_cnt - len(plants)


s = Solution()
print(s.minimumOperations(plants=[7, 7, 7, 7, 7, 7, 7], capacity=8))
print(s.minimumOperations(plants=[1, 1, 1, 4, 2, 3], capacity=4))
print(s.minimumOperations(plants=[2, 2, 3, 3], capacity=5))
