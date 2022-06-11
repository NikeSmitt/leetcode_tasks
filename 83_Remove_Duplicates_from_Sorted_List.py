# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        prev = current = head
        while current is not None:
            if prev.val != current.val:
                prev.next = current
                prev = current
            current = current.next
        prev.next = None
        return head
    
    def test_solution(self):
        h = ListNode(1, ListNode(1, ListNode(2)))
        res = self.delete_duplicates(h)
        h = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        res = self.delete_duplicates(h)


if __name__ == '__main__':
    s = Solution()
    s.test_solution()