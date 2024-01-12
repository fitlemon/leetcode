"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.

The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        right = fast = head
        left = None
        if head.next.next is None:
            return head.val + head.next.val
        while fast:
            fast = fast.next.next
            right.next, right, left = left, right.next, right

        maxSum = 0
        while right:
            maxSum = max(maxSum, right.val + left.val)
            right = right.next
            left = left.next
        return maxSum


# [4,2,2,3]
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
sl = Solution()
print(sl.pairSum(head))
