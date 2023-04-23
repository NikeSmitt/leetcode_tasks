"""

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

"""
from collections import deque


class MinStack:
    
    def __init__(self):
        self.deque = deque([])
        self.min_el = None
    
    def push(self, val: int) -> None:
        if self.min_el is None:
            self.min_el = val
            self.deque.appendleft(val)
        else:
            if val < self.min_el:
                self.deque.appendleft(val * 2 - self.min_el)
                self.min_el = val
            else:
                self.deque.appendleft(val)
    
    def pop(self) -> None:
        el = self.deque.popleft()
        if el < self.min_el:
            pop_el = self.min_el
            self.min_el = self.min_el * 2 - el
        else:
            pop_el = el
        if not len(self.deque):
            self.min_el = None
        return pop_el
    
    def top(self) -> int:
        if self.deque[0] < self.min_el:
            return self.min_el
        return self.deque[0]
    
    def getMin(self) -> int:
        return self.min_el
