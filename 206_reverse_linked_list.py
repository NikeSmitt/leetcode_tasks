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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        
        while cur is not None:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
            
        return prev
    
if __name__ == '__main__':
    s = Solution()
    
    l = ListNode(1, ListNode(2, ListNode(3)))
    print(s.reverseList(l))