# Given the root of a binary tree, return the preorder traversal of its nodes' values.


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: TreeNode, acc: list):
            if node is not None:
                acc.append(node.val)
                dfs(node.left, acc)
                dfs(node.right, acc)
            return acc
        
        return dfs(root, [])
    
    
if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(
        1,
        right=TreeNode(
            2,
            left=TreeNode(3)
        )
    )
    print(s.preorderTraversal(tree))
    print(s.preorderTraversal(None))
    print(s.preorderTraversal(TreeNode(1)))
    
    
