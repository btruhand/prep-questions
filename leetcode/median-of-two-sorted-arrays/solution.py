from typing import List
import math


class Solution:

    def medianFromSortedArray(self, arr: List[int]) -> float:
        midpoint = len(arr) // 2
        if len(arr) % 2 == 0:
            return (arr[midpoint] + arr[midpoint - 1]) / 2
        else:
            return arr[midpoint]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return self.medianFromSortedArray(nums2)
        elif len(nums2) == 0:
            return self.medianFromSortedArray(nums1)

        prevValue1 = None
        midPoint1 = len(nums1) // 2
        low1 = 0
        high1 = len(nums1) - 1
        nextValue1 = None if len(nums1) == 0 else nums1[midPoint1]
        currentValue1 = nextValue1

        prevValue2 = None
        midPoint2 = len(nums2) // 2
        low2 = 0
        high2 = len(nums2) - 1
        nextValue2 = None if len(nums2) == 0 else nums2[midPoint2]
        currentValue2 = nextValue2

        run = True
        while run:
            prevMidpoint1 = midPoint1
            prevMidpoint2 = midPoint2
            if nextValue1 < nextValue2:
                # print("nextValue1 < nextValue2")
                # go right on nums1, left on nums2)
                low1, midPoint1 = midPoint1, (midPoint1 + high1) // 2
                high2, midPoint2 = midPoint2, (low2 + midPoint2) // 2
            else:
                # print("nextValue1 >= nextValue2")
                # go left on nums1, right on nums2
                high1, midPoint1 = midPoint1, (low1 + midPoint1) // 2
                low2, midPoint2 = midPoint2, (midPoint2 + high2) // 2

            print("midpoints", prevMidpoint1,
                  midPoint1, prevMidpoint2, midPoint2)
            nextValue1 = nums1[midPoint1]
            nextValue2 = nums2[midPoint2]

            # if midPoint1 != prevMidpoint1:
            prevValue1, currentValue1 = currentValue1, nextValue1
            # if midPoint2 != prevMidpoint2:
            prevValue2, currentValue2 = currentValue2, nextValue2

            # if (midPoint1 == high1 and midPoint2 == low2) or (midPoint1 == low1 and midPoint2 == high2):
            if midPoint1 == prevMidpoint1 or midPoint2 == prevMidpoint2:
                run = False

        print(prevValue1, currentValue1, prevValue2, currentValue2)
        num1Median = prevValue1 if prevValue1 > currentValue1 else currentValue1
        num2Median = prevValue2 if prevValue2 > currentValue2 else currentValue2
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (num1Median + num2Median) / 2
        else:
            return num1Median if num1Median < num2Median else num2Median


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
    print(solution.findMedianSortedArrays([3, 5, 7], [1, 2, 4, 6, 7]))
    print(solution.findMedianSortedArrays([], [1]))
    print(solution.findMedianSortedArrays([], [1, 2, 3]))
    print(solution.findMedianSortedArrays([], [1, 2, 3, 4, 5, 6]))
    print(solution.findMedianSortedArrays([1], []))
    print(solution.findMedianSortedArrays([1, 2, 3], []))
    print(solution.findMedianSortedArrays([1, 2, 3, 4, 5, 6], []))
    print(solution.findMedianSortedArrays([3], [-2, -1]))
    print('--------------')
    print(solution.findMedianSortedArrays([1, 2, 3, 5, 7], [4, 6, 8, 9]))
    print(solution.findMedianSortedArrays([1, 2], [-1, 3]))
