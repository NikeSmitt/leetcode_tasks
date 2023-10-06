"""You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a
binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13. For all
leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these
numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return self.val
    
    @staticmethod
    def create_tree(values, i=0):
        if i < len(values):
            node: TreeNode = TreeNode(values[i])
            node.left = TreeNode.create_tree(values, i * 2 + 1)
            node.right = TreeNode.create_tree(values, i * 2 + 2)
            return node
        


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == '__main__':
    s = Solution()
    
    # tree = TreeNode(1,
    #                 left=TreeNode(0,
    #                               left=TreeNode(0),
    #                               right=TreeNode(1),
    #                               ),
    #                 right=TreeNode(1,
    #                                left=TreeNode(0),
    #                                right=TreeNode(1))
    #                 )
    
    tree = TreeNode.create_tree([1,0,1,0,1,0,1])
    print(tree)
    r = s.sumRootToLeaf(tree)
    print(r)
