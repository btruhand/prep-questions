from typing import List
import unittest

class Solution:
	"""Solution class to wave array problem

	Please see: `wave array problem <https://www.interviewbit.com/problems/wave-array/>`_
	"""

	def wave(self, A: List[int]) -> List[int]:
		"""Wave function

		Creates a wave array from an integer

		:param A: An array pf integers
		:type A: List[int]
		:return: The wave array result
		:rtype: List[int]
		"""
		A.sort()
		lengthOfA = len(A)
		for idx in range(1, lengthOfA, 2):
			temp = A[idx - 1]
			A[idx - 1] = A[idx]
			A[idx] = temp

		return A

class WaveArrayTest(unittest.TestCase):
	def setup(self):
		self.solution = Solution()

	def test_sample_input(self):
		self.setup()
		self.assertEqual([2,1,4,3], self.solution.wave([1, 2, 3 ,4]))

	def test_unsorted_array(self):
		self.setup()
		self.assertEqual([7,2,12,10,100,87], self.solution.wave([12,7,100,2,87,10]))

	def test_empty_array(self):
		self.setup()
		self.assertEqual([], self.solution.wave([]))

	def test_odd_length_array(self):
		self.setup()
		self.assertEqual([10,6,75,51,83], self.solution.wave([75,51,83,10,6]))

	def test_array_with_duplicate_values(self):
		self.setup()
		self.assertEqual([3,2,4,4,6,5,6], self.solution.wave([6,2,5,3,4,4,6]))

unittest.main()
