# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node: TreeNode, n=0):
            if node is None:
                return n
            return max(depth(node.left, n + 1), depth(node.right, n + 1))
        
        return depth(root)
        


if __name__ == '__main__':
    tree = TreeNode(
        1,
        None,
        TreeNode(2)
    )
    s = Solution()
    print(s.maxDepth(tree))
    print(s.maxDepth(None))
