# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        vals = []

        while cur:
            vals.append(cur.val)
            cur = cur.next

        i = 0
        n = len(vals) - 1
        res = 0

        while i < n:
            res = max(res, vals[i] + vals[n])
            i+=1
            n-=1

        return res