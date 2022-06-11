# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.val


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def dfs(node: Optional[TreeNode], acc: list):
            if node is not None:
                dfs(node.left, acc)
                acc.append(node.val)
                dfs(node.right, acc)
        
        dfs(root, output)
        return output
    
    def test_solution(self):
        root = TreeNode(
            1,
            left=None,
            right=TreeNode(
                2,
                left=TreeNode(3)
            )
        )
        assert [1, 3, 2] == self.inorder_traversal(root)
        assert [] == self.inorder_traversal(None)
        assert [1] == self.inorder_traversal(TreeNode(1))


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
