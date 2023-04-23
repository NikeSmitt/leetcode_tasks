# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        output = f'{self.val}'
        current = self.next
        while current:
            output = f'{output} -> {current.val}'
            current = current.next
        return output


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        current = head
        
        while runner is not None:
            if runner.next is not None:
                runner = runner.next
            else:
                return current
            runner = runner.next
            current = current.next
            
        return current
        

if __name__ == '__main__':
    s = Solution()

    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(s.middleNode(l))

    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print(s.middleNode(l))
    