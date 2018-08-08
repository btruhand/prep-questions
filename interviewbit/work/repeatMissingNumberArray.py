from typing import List
import unittest
import math

class Solution:
	def repeatedNumber(self, A: List[int, int]) -> List[int, int]:
		"""Finding repeated number

		Given a list of integers 1 to n (size of array is n), there is an integer A that
		is repeated. Find the duplicate number A and find B, the number which should have
		been there

		.. note::
			Please see `problem <https://www.interviewbit.com/problems/repeat-and-missing-number-array/>`_

		:param A: List of integers with duplicate A and missing integer B
		:type A: List[int, int]
		:return: Returns A and B
		:rtype: List[int]
		"""
		expectedSum = sum(range(1, len(A) + 1))
		realSum = sum(A)
		expectedSquaredDifference = 0
		for idx, value in enumerate(A):
			expectedSquaredDifference = expectedSquaredDifference + value ** 2 - (idx + 1) ** 2

		expectedDifference = realSum - expectedSum
		duplicate = (expectedSquaredDifference // expectedDifference) + expectedDifference
		duplicate = duplicate // 2
		missing = duplicate - (expectedDifference) # minus because expectedDifference is negative

		return [duplicate, missing]

class TestRepeatMissingNumberArray(unittest.TestCase):
	def setUp(self):
		self.s = Solution()

	def test_simple_case(self):
		self.assertEqual([2, 3], self.s.repeatedNumber([1,4,2,5,2]))
		self.assertEqual([2, 4], self.s.repeatedNumber([1,3,2,5,2]))
		self.assertEqual([3, 4], self.s.repeatedNumber([3,3,1,5,2]))

unittest.main()