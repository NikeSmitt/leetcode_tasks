# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return f'{self.val} -> {str(self.next)}'
        else:
            return f'{self.val}'


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    runner = head

    for _ in range(n - 1):
        if runner.next:
            runner = runner.next
        else:
            return head

    prev = None
    to_del = head

    while runner.next:
        if not prev:
            prev = head
        else:
            prev = prev.next
        to_del = to_del.next
        runner = runner.next

    # deleting
    if prev:
        prev.next = to_del.next
    else:
        return to_del.next

    return head


if __name__ == '__main__':
    h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(h)

    res = remove_nth_from_end(h, 2)
    print(res)
    #
    #
    h = ListNode(1)
    print(h)
    print(remove_nth_from_end(h, 1))
    #
    #
    h = ListNode(1, ListNode(2))
    print(h)
    print(remove_nth_from_end(h, 1))

    h = ListNode(1, ListNode(2))
    print(h)
    print(remove_nth_from_end(h, 2))
