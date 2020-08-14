from typing import List


class Solution:
    def find_rotation_point(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)

        while left < right - 1:  # since left is not updated as mid + 1 then we have to do this
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                # normal case
                left = mid  # not mid + 1 because then we might skip over the rotation point
            else:
                right = mid
        return left + 1

    def search(self, nums: List[int], target: int) -> int:
        """Found it easiest to just search for the rotation point and then use that
        knowledge later on if needed (maybe can save time by doing it later).

        If we reach the end of the array we want to look to the left of the rotation point
        If we reach the beginning we want to look to the right of the rotation point 

        If we haven't returned at the end, then we can't find it
        """
        left = 0
        right = len(nums)
        rotated = False  # marker to only do rotation check once

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid

            if not rotated and left == right and left == len(nums) and nums[0] >= nums[mid]:
                # rotation
                left, right = 0, self.find_rotation_point(nums)
                rotated = True
            elif not rotated and left == right and right == 0 and nums[len(nums) - 1] <= nums[mid]:
                # rotation
                left, right = self.find_rotation_point(nums), len(nums)
                rotated = True

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 4) == 0)
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1)
    print(solution.search([], 1) == -1)
    print(solution.search([0, 1, 2, 4, 6], 5) == -1)
    print(solution.search([0, 1, 2, 4, 6], 6) == 4)
    print(solution.search([9, 1, 2, 3, 4, 5, 6, 7, 8], 9) == 0)
