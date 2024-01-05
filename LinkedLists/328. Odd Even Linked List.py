"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        odd = odd_head = head
        even = even_head = head.next
        curr = head.next
        while curr:
            if curr.next:
                odd.next = curr.next
                odd = odd.next
            else:
                break
            if curr.next.next:
                even.next = curr.next.next
                even = even.next
            else:
                break

            curr = even

        odd.next = even_head

        return odd_head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solut = Solution()
print(solut.oddEvenList(head))
