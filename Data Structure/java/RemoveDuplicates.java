/**
 * Given a sorted linked list, delete all duplicates such that each element
 * appear only once.
 * 
 * Example: Input: 1->1->2 Output: 1->2
 * 
 * Input: 1->1->2->3->3 Output: 1->2->3
 */

// Definition for singly-linked list.
public class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

public class RemoveDuplicates {
    /**
     * 
     * @param head: the begining ListNode of LinkedList.
     * @return the head of LinkedList without duplicates.
     * 
     *         Time Complexity: O(n), Space Complexity: O(1)
     */
    public ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head, res = head;
        while (cur != null) {
            while (cur.next != null && cur.next.val == cur.val) {
                cur.next = cur.next.next;
            }
            cur = cur.next;
        }
        return res;
    }
}