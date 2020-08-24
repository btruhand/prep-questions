from typing import List


class Solution:
    """
    Solution uses recursion and builds up results by an accumulator. While we can continue to open
    a parantheses we can continue to try opening parantheses, which then should be closed (hence the
    next if statement).
    Closing a parantheses requires opening a parantheses first, so the count of opened parantheses
    MUST be smaller than the number of closing parantheses left
    """

    def helper(self, nOpen: int, nClose: int, acc: str, collection: List[str]):
        if nOpen == 0 and nClose == 0:
            collection.append(acc)
        else:
            if nOpen != 0:
                self.helper(nOpen - 1, nClose, acc + '(', collection)
            if nClose != 0 and nClose > nOpen:
                self.helper(nOpen, nClose - 1, acc + ')', collection)

    def generateParenthesis(self, n: int) -> List[str]:
        collection = []
        self.helper(n, n, '', collection)
        return collection


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
    print(solution.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ])
