class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class RevLinkList {
    public ListNode reverseList(ListNode head) {
        ListNode newTemp = new ListNode(head.val);
        ListNode temp = head;

        while (temp.next != null) {
            ListNode copy = new ListNode(newTemp.val, newTemp.next);
            newTemp = new ListNode(temp.next.val, copy);
            temp = temp.next;
        }

        return newTemp;
    }

    public static void main(String[] args) {
        // Example usage
        ListNode head = new ListNode(0);
        head.next = new ListNode(1);
        head.next.next = new ListNode(2);
        head.next.next.next = new ListNode(3);

        RevLinkList solution = new RevLinkList();
        ListNode reversed = solution.reverseList(head);

        // Print reversed list
        while (reversed != null) {
            System.out.print(reversed.val + " ");
            reversed = reversed.next;
        }
    }
}