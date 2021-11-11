from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prv_val = head.val
        head = head.next

        current_idx = 1
        First = None
        Last = None
        mi = float('inf')

        while head.next:
            if prv_val < head.val > head.next.val or prv_val > head.val < head.next.val:
                if not First:
                    First = current_idx
                else:
                    mi = min(mi, current_idx - Last)

                Last = current_idx
            current_idx += 1
            prv_val = head.val
            head = head.next

        if mi == float('inf'):
            return [-1, -1]
        else:
            return [mi, Last - First]
