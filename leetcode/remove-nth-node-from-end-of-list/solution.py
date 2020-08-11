# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, value):
        curr_self = self
        while curr_self is not None and value is not None:
            if curr_self.val != value.val:
                return False
            curr_self = curr_self.next
            value = value.next

        return curr_self is None and value is None


class Solution:
    """
    use two pointers to solve. First pointer is found by moving n times ahead of the list. Second pointer
    is simply from the start of the list. Then just keep moving forward till the pointer that was ahead
    reaches None. The distance between the first and second pointer will be n nodes, so the second pointer
    will be pointing to the n-th node from the end of the list. From there just do some re-attachments
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        ahead = head
        while i < n:
            ahead = ahead.next
            i += 1

        original_head = head
        prev = None
        while ahead is not None:
            prev = head
            head = head.next
            ahead = ahead.next

        if prev is None:
            return head.next
        prev.next = head.next
        return original_head


if __name__ == "__main__":
    solution = Solution()

    print(solution.removeNthFromEnd(
        ListNode(1,
                 ListNode(2,
                          ListNode(3,
                                   ListNode(4, ListNode(5))))), 2) == ListNode(1, ListNode(2, ListNode(3, ListNode(5)))))
    print(solution.removeNthFromEnd(ListNode(1), 1) is None)
    print(solution.removeNthFromEnd(ListNode(1, ListNode(2)), 2) == ListNode(2))
