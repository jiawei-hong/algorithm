# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev, cur = head, head.next

        while prev and cur:
            prev.val, cur.val = cur.val, prev.val

            if cur.next is None or cur.next.next is None:
                break

            prev = cur.next
            cur = cur.next.next

        return head
