import unittest

class Solution:
	def firstMissingPositive(self, A):
		length_of_A = len(A)
		idx = 0
		while idx < length_of_A:
			value = A[idx]
			if 1 <= value <= length_of_A:
				if value >= idx + 1:
					A[idx], A[value - 1] = A[value - 1], value
				else:
					A[idx], A[value - 1] = 0, value
			else:
				A[idx] = 0
			if A[idx] == 0 or A[idx] == idx + 1:
				idx = idx + 1

		for idx, value in enumerate(A):
			if value == 0:
				return idx + 1

		return length_of_A + 1

class TestFindFirstNonNegative(unittest.TestCase):
	def setUp(self):
		self.s = Solution()

	def test_sample_input(self):
		self.assertEqual(3, self.s.firstMissingPositive([1,2,0]))
		self.assertEqual(2, self.s.firstMissingPositive([3,4,-1,1]))
		self.assertEqual(1, self.s.firstMissingPositive([-8,-7,-6]))

	def test_more_than_one_negative(self):
		self.assertEqual(3, self.s.firstMissingPositive([2,4,-3,1,-5,6]))
		self.assertEqual(3, self.s.firstMissingPositive([-3,4,6,2,-5,1]))

	def test_complete_in_array(self):
		self.assertEqual(5, self.s.firstMissingPositive([3,2,4,1]))

	def test_element_out_of_bounds_in_array(self):
		self.assertEqual(1, self.s.firstMissingPositive([5,3,4,2,6,8,7]))

	def test_repeated_values(self):
		self.assertEqual(3, self.s.firstMissingPositive([1,2,2,1,1,2,1]))

unittest.main()