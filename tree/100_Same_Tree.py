# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        
    
    def test_solution(self):
        assert self.is_same_tree(None, None)
        assert not self.is_same_tree(TreeNode(), None)
        assert not self.is_same_tree(TreeNode(0, TreeNode(-5)), TreeNode(0, TreeNode(-8)))
        assert self.is_same_tree(TreeNode(1, TreeNode(2)), TreeNode(1, TreeNode(2)))
        assert not self.is_same_tree(TreeNode(1, TreeNode(1)), TreeNode(1, None, TreeNode(1)))


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
