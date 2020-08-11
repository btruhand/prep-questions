from typing import List

# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def calculateArea(self, a1, a2, i1, i2):
        width = i1 - i2
        width = -width if width < 0 else width
        height = min([a1, a2])
        return height * width

    # Basically have two pointers starting from beginning and end of list
    # Compute the area between the two pointers and assign it as max if it is greater than max
    # Step "forward" according to the height of the currently pointed values
    # The one with lesser height should be step forwarded, because we want to find a height
    # that is greater than the current smaller one (and if we move the greater one, it can only
    # affect things if the next one is smaller, and that would DEFINITELY cause a non maximum area)
    def maxArea(self, height: List[int]) -> int:
        i1, i2 = 0, len(height) - 1
        max_area = 0
        while i1 < i2:
            max_area = max(max_area, self.calculateArea(
                height[i1], height[i2], i1, i2))
            if height[i1] < height[i2]:
                i1 += 1
            else:
                i2 -= 1
        return max_area


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
    print(solution.maxArea([2, 3, 4]) == 4)
    print(solution.maxArea([2, 2]) == 2)
    print(solution.maxArea([3, 2, 6, 5, 4]) == 12)
    print(solution.maxArea([1, 2, 3, 8, 4, 5, 8, 6]) == 24)
    print(solution.maxArea([2, 1, 4, 3, 5, 4]) == 12)
    print(solution.maxArea([2, 1, 5, 3, 2]) == 8)
    print(solution.maxArea([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25)
    print(solution.maxArea([8, 10, 14, 0, 13, 10, 9, 9, 11, 11]) == 80)
    print(solution.maxArea([5, 2, 12, 1, 5, 3, 4, 11, 9, 4]) == 55)
    print(solution.maxArea([1, 2, 3, 4, 5, 25, 24, 3, 4]) == 24)
    print(solution.maxArea([1, 3, 2, 5, 25, 24, 5]) == 24)
