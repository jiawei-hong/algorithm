# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid_node = self.get_mid_node(head)
        mid_reversed_node = self.get_mid_reversed_node(mid_node.next)

        while mid_reversed_node:
            if head.val == mid_reversed_node.val:
                head = head.next
                mid_reversed_node = mid_reversed_node.next
            else:
                return False
        return True

    def get_mid_node(self, node: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = node

        slow = dummy
        fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def get_mid_reversed_node(self, node: ListNode) -> ListNode:
        curr, prev = node, None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
