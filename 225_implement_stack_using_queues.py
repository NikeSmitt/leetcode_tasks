from collections import deque


class MyStack:
    
    def __init__(self):
        self._deque = deque()
    
    def push(self, x: int) -> None:
        self._deque.append(x)
    
    def pop(self) -> int:
        return self._deque.pop()
    
    def top(self) -> int:
        if not self.empty():
            return self._deque[-1]
    
    def empty(self) -> bool:
        return False if len(self._deque) else True


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    res = obj.top()
    res = obj.pop()
    res = obj.empty()
    
    