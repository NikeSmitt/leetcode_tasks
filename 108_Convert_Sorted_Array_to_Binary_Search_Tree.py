from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_to_bst(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = self.sorted_array_to_bst(nums[:mid])
            root.right = self.sorted_array_to_bst(nums[mid + 1:])
            return root


if __name__ == '__main__':
    s = Solution()
    tree = s.sorted_array_to_bst([-10, -3, 0, 5, 9])
    tree = s.sorted_array_to_bst([1])