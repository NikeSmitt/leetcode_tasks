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
    
    def __init__(self, ver=1):
        match ver:
            case 1:
                
                self.invertTree = self._invert_tree_ver_1
            case 2:
                self.invertTree = self._invert_tree_ver_2
    
    def _invert_tree_ver_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return root
    
    def _invert_tree_ver_2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self._invert_tree_ver_2(root.left)
        self._invert_tree_ver_2(root.right)
        
        root.left, root.right = root.right, root.left
        return root


if __name__ == '__main__':
    a = [4, 2, 7, 1, 3, 6, 9]
    tree = TreeNode.create_tree(a)
    s = Solution(ver=2)
    root = s.invertTree(tree)
    print(root)
