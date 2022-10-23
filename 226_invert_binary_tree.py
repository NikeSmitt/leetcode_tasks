from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @classmethod
    def create_tree(cls, array: list):
        
        root = TreeNode(array[0])
        tree_level = [root]
        idx = 1
        
        while idx < len(array):
            left = right = None
            node = tree_level.pop(0)
            left = TreeNode(array[idx])
            idx += 1
            if idx < len(array):
                right = TreeNode(array[idx])
            idx += 1
            node.left, node.right = left, right
            tree_level.extend([left, right])
        
        return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass


if __name__ == '__main__':
    a = [4, 2, 7, 1, 3, 6, 9]
    tree = TreeNode.create_tree(a)
    print(tree)