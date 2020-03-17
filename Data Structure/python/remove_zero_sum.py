# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
    After doing so, return the head of the final linked list.  You may return any such answer.
    (Note that in the examples below, all sequences are serializations of ListNode objects.)

    Example:
        Input: head = [1,2,-3,3,1]
        Output: [3,1]

        Input: head = [1,2,3,-3,4]
        Output: [1,2,4]

        Input: head = [1,2,3,-3,-2]
        Output: [1]
    """

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        """
        Args:
            head: head of Linked list

        Return:
            head of Linked list without zero sum consecutive nodes.

        Idea of solution:
            Use a hashtable to store the first ListNode* that has a given prefix sum.
            Whenever the same prefix sum occurs, skip all the elements between the first
            occurrence and current one, e.g. first_sum_x.next = curr_sum_x.next

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        dummy = ListNode(0)
        dummy.next = head
        pre_sum = 0
        seen = {0: dummy}
        while head:
            pre_sum += head.val
            seen[pre_sum] = head
            head = head.next
        head = dummy
        pre_sum = 0
        while head:
            pre_sum += head.val
            head.next = seen[pre_sum].next
            head = head.next
        return dummy.next
