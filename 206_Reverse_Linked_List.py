from typing import Optional


# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.
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
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current, next_ = None, head, head
        
        while current is not None:
            next_ = next_.next
            current.next = prev
            prev = current
            current = next_
        
        return prev


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
