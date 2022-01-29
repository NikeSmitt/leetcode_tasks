# Definition for a Node.
from typing import Optional
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root is None:
            return

        queue = deque([root])
        temp_node = None

        while queue:
            n = len(queue)
            for i in range(n):

                prev_node = temp_node
                temp_node = queue.popleft()

            # i > 0 because when i is 0 prev points
            # the last node of previous level,
            # so we skip it

                if i > 0:
                        prev_node.next = temp_node

                if temp_node.left is not None:
                    queue.append(temp_node.left)

                if temp_node.right is not None:
                    queue.append(temp_node.right)

        return root


if __name__ == '__main__':
    task = Solution()

    tree = Node(1,
                left=Node(2,
                          left=Node(4),
                          right=Node(5)
                          ),
                right=Node(3,
                           left=Node(6),
                           right=Node(7)
                           )
                )

    res = task.connect(tree)

    res = task.connect(None)


