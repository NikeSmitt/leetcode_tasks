# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node: TreeNode, n=0):
            if node is None:
                return n - 1
            return max(depth(node.left, n + 1), depth(node.right, n + 1))
        
        def helper(node, acc):
            if node is not None:
                d_l = depth(node.left)
                d_r = depth(node.right)
                acc.append(abs(d_r - d_l) < 2)
                helper(node.left, acc)
                helper(node.right, acc)
        
        res = []
        helper(root, res)
        return all(res)


if __name__ == '__main__':
    tree = TreeNode(
        3,
        left=TreeNode(9),
        right=TreeNode(
            20,
            left=TreeNode(15),
            right=TreeNode(7)
        )
    )
    
    s = Solution()
    print(s.isBalanced(tree))
    
    tree = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(
                3,
                TreeNode(4),
                TreeNode(4)
            ),
            TreeNode(3)
        ),
        TreeNode(2)
    )
    
    print(s.isBalanced(tree))
    print(s.isBalanced(None))
