# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x, next_: Optional['ListNode'] = None):
        self.val = x
        self.next = next_
    
    def add(self, node: 'ListNode'):
        tail = self
        while tail.next is not None:
            tail = tail.next
        tail.next = node
        
    def __str__(self):
        return f'{self.val}'
            

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        runner, turtle = head, head
        
        while runner is not None:
            
            runner = runner.next
            if runner is not None:
                runner = runner.next
                turtle = turtle.next
                if runner is turtle:
                    runner = head
                    while runner is not turtle:
                        runner = runner.next
                        turtle = turtle.next
    
                    return turtle
        
            
         
            
        runner = head
        while runner is not turtle:
            runner = runner.next
            turtle = turtle.next
            
        return turtle
        
        
        
        
        
        

if __name__ == '__main__':
    s = Solution()
    cycle = ListNode(2)
    l = ListNode(3)
    l.add(cycle)
    l.add(ListNode(0))
    l.add(ListNode(-4, cycle))
    
    print(s.detectCycle(l))
    
    l = ListNode(1)
    l.add(ListNode(2, l))
    print(s.detectCycle(l))
