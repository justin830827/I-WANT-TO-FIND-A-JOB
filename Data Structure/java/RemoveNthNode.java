/**
 * Given a linked list, remove the n-th node from the end of list and return its
 * head.
 * 
 * Time Complexity: O(n), Space Complextity: O(1)
 */

public class RemoveNthNode {
    public static class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    /**
     * 
     * @param head: head of Linked list
     * @param n:    an integer to indicate the Nth node to be removed from end of
     *              list.
     * @return the head of ListNode with Nth node has been removed.
     */
    public ListNode twoPassRemoval(ListNode head, int n) {
        // count the length of Linked List
        int l = 0;
        ListNode h = head;
        while (h != null) {
            h = h.next;
            l++;
        }

        // Handle Corner Case
        int diff = l - n;
        if (diff == 0) {
            return head.next;
        }

        // Remove nth node
        ListNode res = head;
        for (int i = 0; i < diff - 1; i++) {
            head = head.next;
        }
        head.next = head.next.next;
        return res;
    }

    /**
     * 
     * @param head: head of Linked list
     * @param n:    an integer to indicate the Nth node to be removed from end of
     *              list.
     * @return the head of ListNode with Nth node has been removed.
     */
    public ListNode onePassRemoval(ListNode head, int n) {
        ListNode slow = head, fast = head;
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }
        if (fast == null)
            return head.next;
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return head;
    }
}