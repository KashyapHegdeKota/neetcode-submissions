# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        slow.next = None

        l2 = self.reverse(l2)
        l1 = head
        self.merge(l1,l2)


    def reverse(self, middle: Optional[ListNode]) -> ListNode:
        prev = None
        curr = middle

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        return prev
    
    def merge(self, l1, l2) -> ListNode:
        while l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2