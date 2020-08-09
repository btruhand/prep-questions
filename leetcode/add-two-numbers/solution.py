# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def length(self):
        count = 0
        curr = self
        while curr is not None:
            count += 1
            curr = self.next
        return count

    def int_val(self):
        value = 0
        tens = 1
        curr = self
        while curr is not None:
            value += tens * curr.val
            tens *= 10
            curr = curr.next
        return value


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_over = 0
        res = None
        next = None
        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            total = carry_over + val1 + val2
            carry_over = total // 10
            total = total % 10

            if res is None:
                res = next = ListNode(total)
            else:
                new_node = ListNode(total)
                next.next = new_node
                next = new_node
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry_over != 0:
            next.next = ListNode(carry_over)
        return res


if __name__ == "__main__":
    solution = Solution()

    print(solution.addTwoNumbers(
        ListNode(1, ListNode(2)), ListNode(3)).int_val() == 24)
    print(solution.addTwoNumbers(
        ListNode(0), ListNode(3)).int_val() == 3)
    print(solution.addTwoNumbers(
        ListNode(0), ListNode(0)).int_val() == 0)
    print(solution.addTwoNumbers(
        ListNode(1, ListNode(0, ListNode(2))),
        ListNode(2, ListNode(4, ListNode(4)))).int_val() == 643)
    print(solution.addTwoNumbers(ListNode(9), ListNode(9)).int_val() == 18)
