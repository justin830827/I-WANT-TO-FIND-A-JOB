# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Given a linked list, remove the n-th node from the end of list and return its head.

    Example:
        Input: linked list 1->2->3->4->5, and n = 2.
        Output: 1->2->3->5.

    Note:
        Given n will always be valid.
    """

    def removeNthFromEnd_two_pass(self, head: ListNode, n: int) -> ListNode:
        """
        Args:
            head: head of Linked list
            n: an integer to indicate the Nth node to be removed from end of list.
        Return:
            the head of ListNode with Nth node has been removed.

        Idea of solution:
            First pass to get the length of Linked list, second pass to remove the nth node.

        Time Complextiy: O(n), where n = length of Linked list
        Space Complexity: O(1)
        """
        # Get Length of LinkedList
        h = head
        l = 0  # length
        while h:
            l += 1
            h = h.next
        diff = l - n

        # Corner Case
        if diff == 0:
            return head.next

        # Remove node
        res = head
        for i in range(diff - 1):
            head = head.next
        head.next = head.next.next

        return res

    def removeNthFromEnd_one_pass(self, head: ListNode, n: int) -> ListNode:
        """
        Args:
            head: head of Linked list
            n: an integer to indicate the Nth node to be removed from end of list.
        Return:
            the head of ListNode with Nth node has been removed.

        Idea of solution:
            Use an array to record each node to and remove

        Time Complextiy: O(n), where n = length of Linked list
        Space Complexity: O(n)
        """
        nodes = []
        res = head
        while head:
            nodes.append(head)
            head = head.next
        if len(nodes) == n:
            return res.next
        nodes[-n-1].next = nodes[-n-1].next.next
        return res

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Best Solution
        Args:
            head: head of Linked list
            n: an integer to indicate the Nth node to be removed from end of list.
        Return:
            the head of ListNode with Nth node has been removed.

        Idea of solution:
            Use two pointer to keep the first pointer and second pointer with n distance

        Time Complextiy: O(n), where n = length of Linked list
        Space Complexity: O(n)
        """
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        # if fast is None then we know we remove the first node
        if not fast:
            return fast.next
        # fast will stop on the last node and slow will stop after (n - 1)th node
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
