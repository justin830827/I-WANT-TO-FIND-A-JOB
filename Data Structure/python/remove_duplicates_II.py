# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given a sorted linked list, delete all nodes that have duplicate numbers,
    leaving only distinct numbers from the original list. Return the linked
    list sorted as well.

    Example:
        Input: 1->2->3->3->4->4->5
        Output: 1->2->5

        Input: 1->1->1->2->3
        Output: 2->3

    Idea of solution:
        1. A head of linked list named cur to loop over and remove the duplicates.
        2. We create a dummy node as previous node.
        3. if pre.next == cur means that the current node is not a duplicated node. 
        Otherwise, we skip the duplicated node by pre.next = cur.next.
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
        cur = head
        res = pre = ListNode(0, head)
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return res.next
