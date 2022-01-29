# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while fast.next:
        if fast.next.next:
            fast = fast.next.next
        else:
            return slow.next
        slow = slow.next
    return slow


