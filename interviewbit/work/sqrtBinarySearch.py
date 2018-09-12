import unittest

class Solution:
	def sqrt(self, A: int) -> int:
		"""sqrt function using binary search

		Finds the approximate square root of A.

		.. note::
			Please refer to `<https://www.interviewbit.com/problems/square-root-of-integer/>`_
			for original problem

		:param A: Integer to take approximate sqrt of
		:type A: int
		"""
		original = A
		lower_bound = 1
		upper_bound = A
		while (A + 1) ** 2 <= original or A ** 2 > original:
			if A ** 2 > original:
				A = (upper_bound + lower_bound) // 2
				upper_bound = A
			else:
				lower_bound = A
				A = A * 2
				upper_bound = A

		return A

class TestSqrtBinarySearch(unittest.TestCase):
	def setUp(self):
		self.s = Solution()

	def test_non_perfect_square(self):
		self.assertEqual(1, self.s.sqrt(2))
		self.assertEqual(1, self.s.sqrt(3))
		self.assertEqual(2, self.s.sqrt(6))
		self.assertEqual(2, self.s.sqrt(7))
		self.assertEqual(2, self.s.sqrt(8))
		self.assertEqual(3, self.s.sqrt(9))
		self.assertEqual(3, self.s.sqrt(11))
		self.assertEqual(22, self.s.sqrt(525))
		self.assertEqual(10, self.s.sqrt(101))
		self.assertEqual(1003, self.s.sqrt(1007010))

	def test_perfect_square(self):
		self.assertEqual(1, self.s.sqrt(1))
		self.assertEqual(4, self.s.sqrt(16))
		self.assertEqual(5, self.s.sqrt(25))
		self.assertEqual(13, self.s.sqrt(169))

unittest.main()