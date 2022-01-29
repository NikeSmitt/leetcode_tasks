"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return f'{self.val} -> {str(self.next)}'
        else:
            return f'{self.val}'


class Solution:
    @staticmethod
    def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer_1, pointer_2 = list1, list2
        prev_node = ListNode()
        head = prev_node
        while pointer_1 and pointer_2:
            if pointer_1.val < pointer_2.val:
                prev_node.next = pointer_1
                prev_node = prev_node.next
                pointer_1 = pointer_1.next

            else:
                prev_node.next = pointer_2
                prev_node = prev_node.next
                pointer_2 = pointer_2.next

        while pointer_2:
            prev_node.next = pointer_2
            prev_node = prev_node.next
            pointer_2 = pointer_2.next

        while pointer_1:
            prev_node.next = pointer_1
            prev_node = prev_node.next
            pointer_1 = pointer_1.next

        return head.next


l_1 = ListNode(1, ListNode(2, ListNode(4)))
l_2 = ListNode(1, ListNode(3, ListNode(4)))

print(Solution.merge_two_lists(l_1, l_2))

print(Solution.merge_two_lists(None, None))
print(Solution.merge_two_lists(None, ListNode(0)))

