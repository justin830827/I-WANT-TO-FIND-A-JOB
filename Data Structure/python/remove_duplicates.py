# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given a sorted linked list, delete all duplicates such that each element
    appear only once.

    Example:
        Input: 1->1->2
        Output: 1->2

        Input: 1->1->2->3->3
        Output: 1->2->3
    """

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Args:
            head: the begining ListNode of LinkedList.

        Return:
            the head of LinkedList without duplicates.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return
        res = cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return res
