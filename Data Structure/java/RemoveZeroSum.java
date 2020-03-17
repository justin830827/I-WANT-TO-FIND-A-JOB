import java.util.*;

/**
 * Given the head of a linked list, we repeatedly delete consecutive sequences
 * of nodes that sum to 0 until there are no such sequences.
 * 
 * After doing so, return the head of the final linked list. You may return any
 * such answer.
 * 
 * Idea of solution: Use a hashtable to store the first ListNode* that has a
 * given prefix sum. Whenever the same prefix sum occurs, skip all the elements
 * between the first occurrence and current one, e.g. first_sum_x.next =
 * curr_sum_x.next
 * 
 * Time Complexity: O(n), Space Complexity: O(n)
 */

class RemoveZeroSum {
    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    /**
     * @param head: head of Linked list
     * @return head of Linked list without zero sum consecutive nodes.
     */
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int preSum = 0;
        HashMap<Integer, ListNode> map = new HashMap<>();
        map.put(0, dummy);
        while (head != null) {
            preSum += head.val;
            map.put(preSum, head);
            head = head.next;
        }
        head = dummy;
        preSum = 0;
        while (head != null) {
            preSum += head.val;
            head.next = map.get(preSum).next;
            head = head.next;
        }
        return dummy.next;
    }
}