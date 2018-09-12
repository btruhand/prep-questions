import functools
import unittest

class Solution:
	def order_str_integers(self, x, y):
		if first_option < second_option:
			return -1
		elif first_option == second_option:
			return 0
		else:
			return 1

	def largestNumber(self, A):
		strA = list(map(str, A))
		strA = sorted(strA, key=functools.cmp_to_key(self.order_str_integers), reverse=True)
		print(strA)
		current_result = ''.join(strA)

		if all(map(lambda x: x == '0', current_result)):
			return '0'
		return current_result

class TestLargestNumber(unittest.TestCase):
	def setUp(self):
		self.s = Solution()

	def test_sample_input(self):
		self.assertEqual('9534330', self.s.largestNumber([3, 30, 34, 5, 9]))

	def test_high_in_the_middle(self):
		self.assertEqual('94350324310100', self.s.largestNumber([10, 50, 243, 100, 943, 3]))

	def test_long_input(self):
		self.assertEqual('99197494093090589587787286882579979879178278077273570968668667867566465335024704093953663633573372982927126124019124113', self.s.largestNumber([ 782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357, 261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298, 470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905 ]))
		self.assertEqual('9999899759549499493192290390289987285582981780279771757477437437407167157086996636386155895875234624484023893737234232632332231229288286236209196176163124114103', self.s.largestNumber([ 931, 94, 209, 448, 716, 903, 124, 372, 462, 196, 715, 802, 103, 740, 389, 872, 615, 638, 771, 829, 899, 999, 29, 163, 342, 902, 922, 312, 326, 817, 288, 75, 37, 286, 708, 589, 975, 747, 743, 699, 743, 954, 523, 989, 114, 402, 236, 855, 323, 79, 949, 176, 663, 587, 322 ]))

	def test_equal_until_certain_part(self):
		self.assertEqual('81596596250', self.s.largestNumber([50,596,5962,81]))

	def test_equal_until_certain_part_last_part_is_higher_than_beginning(self):
		self.assertEqual('81596959650', self.s.largestNumber([50,596,5969,81]))

	def test_equal_but_looping(self):
		self.assertEqual('12121', self.s.largestNumber(['121','12']))
		self.assertEqual('12121', self.s.largestNumber(['12','121']))

	def test_equal_to_the_dot(self):
		self.assertEqual('123123', self.s.largestNumber(['123','123']))


unittest.main()