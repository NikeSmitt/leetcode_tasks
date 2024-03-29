"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
"""
from collections import deque


class MyQueue:
    
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.count = 0
    
    def push(self, x: int) -> None:
        if self.count:
            while len(self.s1):
                self.s2.append(self.s1.pop())
                
            self.s1.append(x)
            
            while len(self.s2):
                self.s1.append(self.s2.pop())
                
        else:
            self.s1.append(x)
        
        self.count += 1
    
    def pop(self) -> int:
        if self.count:
            self.count -= 1
            return self.s1.pop()
    
    def peek(self) -> int:
        if self.count:
            return self.s1[-1]
    
    def empty(self) -> bool:
        return not bool(self.count)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
