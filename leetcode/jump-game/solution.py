from typing import List


class Solution:
    """
    The idea is that we can keep going through the list and just get the maximum
    between the old known step - 1 AND the current seen step. Whichever is larger
    tells us how much more we can keep moving. So it becomes an easy job of traversing the
    list in O(n) time
    """

    def canJump(self, nums: List[int]) -> bool:
        current_step = 1
        curr_pos = 0
        end = len(nums)
        while current_step != 0 and curr_pos != end:
            current_step -= 1
            current_step = max(current_step, nums[curr_pos])
            curr_pos += 1

        return curr_pos == end


if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump([2, 3, 1, 1, 4]) == True)
    print(solution.canJump([3, 2, 1, 0, 4]) == False)
