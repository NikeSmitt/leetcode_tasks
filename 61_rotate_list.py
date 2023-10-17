# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        count = 0
        while current is not None:
            count += 1
            current = current.next
            
        if not count or k % count == 0:
            return head
        
        current = head
        prev = None
        for i in range(count - (k % count)):
            prev = current
            current = current.next
        
        prev.next = None
        new_head = current
        while current.next is not None:
            current = current.next
        current.next = head
        return new_head
        
        
        
if __name__ == '__main__':
    s = Solution()
    assert s.rotateRight(None, 0) == None
