# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        s = f'{self.val}'
        current = self
        while current.next:
            current = current.next
            s = f'{s} -> {current.val}'
        return s
    
    @staticmethod
    def create_list(values: list) -> 'ListNode':
        # assert len(values), 'List must not be empty!'
        helper = ListNode(-1, None)
        current = helper
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return helper.next
    
    @staticmethod
    def get_array(node):
        output = []
        current = node
        while current:
            output.append(current.val)
            current = current.next
        
        return output


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        helper = ListNode(-1, None)
        helper.next = head
        prev = helper
        current = head
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return helper.next


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([], 1, []),
        ([7, 7, 7, 7], 7, [])
    ]
    
    s = Solution()
    for arr, target, right_res in test_cases:
        head = ListNode.create_list(arr)
        print(f'Source: {head} | {ListNode.get_array(head)}')
        print(f'Target: {target}')
        
        res = s.removeElements(head, target)
        print(f'Result: {res} | {ListNode.get_array(res)}')
        print('=' * 50)
        
        # assert right_res != res
    
    # head = ListNode.create_list([1, 2, 3])
    # print(head)
    #
    # res = Solution().removeElements(head, 5)
    # print(res)
