from typing import List, Dict
import unittest

class Solution:
	def is_subarray_length_greater(
		self,
		subarray_one_indices: Dict[str, int],
		subarray_two_indices: Dict[str, int]
	) -> bool:
		subarray_one_length = subarray_one_indices['end'] - subarray_one_indices['begin']
		subarray_two_length = subarray_two_indices['end'] - subarray_two_indices['begin']
		return subarray_one_length > subarray_two_length


	def maxset(self, A: List[int]) -> List[int]:
		"""maxset

		Returns a contiguous subarray that only has non-negative integers (including 0)

		.. note::
			Please see `problem set <https://www.interviewbit.com/problems/max-non-negative-subarray/>`_
			for more info

			Runtime complexity: O(n)
			Space complexity: O(1)

		:param A: Given integer list
		:type A: List[int]
		:return: A subarray of A meeting the requirements of the problem
		:rtype: List[int]
		"""

		startingSubarrayIndex = -1
		endingSubarrayIndex = -1
		currentValue = 0
		currentMaximum = 0
		restartIndex = 0
		lastPositiveIndex = -1
		for index, value in enumerate(A):
			if value >= 0:
				currentValue = currentValue + value

				# check for sentinel value
				if startingSubarrayIndex == -1:
					startingSubarrayIndex = index
					restartIndex = index
				lastPositiveIndex = index

			if (value < 0 or index == len(A) - 1) and startingSubarrayIndex != -1:
				# negative and not sentinel
				if currentValue > currentMaximum or\
					(currentValue == currentMaximum and self.is_subarray_length_greater(
						{'begin': restartIndex, 'end': index},
						{'begin': startingSubarrayIndex, 'end': endingSubarrayIndex}
					)):
					currentMaximum, startingSubarrayIndex, endingSubarrayIndex =\
						(currentValue, restartIndex, lastPositiveIndex)

				restartIndex = index + 1
				currentValue = 0

		return A[startingSubarrayIndex:endingSubarrayIndex + 1]


class TestMaxNonNegativeSubArray(unittest.TestCase):
	def setUp(self):
		self.s = Solution()

	def test_empty_array(self):
		self.assertEqual([], self.s.maxset([]))

	def test_sample_input(self):
		self.assertEqual([1,2,5], self.s.maxset([1,2,5,-7,2,3]))

	def test_single_element_nonnegative(self):
		self.assertEqual([0], self.s.maxset([0]))

	def test_single_element_negative(self):
		self.assertEqual([], self.s.maxset([-1]))

	def test_only_nonnegative_elements(self):
		self.assertEqual([1,6,5,10,7], self.s.maxset([1,6,5,10,7]))

	def test_only_negative_elements(self):
		self.assertEqual([], self.s.maxset([-10,-6,-15,-2,-3]))

	def test_negative_element_last(self):
		self.assertEqual([10,20,45], self.s.maxset([10,7,16,-7,10,20,45,-8]))

	def test_multiple_negative_in_a_row(self):
		self.assertEqual([4,5,9], self.s.maxset([5,7,3,-10,-5,4,5,9,-1,-2,-3,9]))

	def test_one_big_integer_in_the_middle(self):
		self.assertEqual([100], self.s.maxset([1,1,5,6,8,-12,-12,100,-1,5,7,8]))

	def test_begin_with_negative(self):
		self.assertEqual([129,7], self.s.maxset([-1,-2,129,7,-1,12]))



unittest.main()