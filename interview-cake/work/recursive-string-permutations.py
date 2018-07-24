import unittest

# Given a string find and return all the permutation of the string
# Implement in a recursive manner

def char_insertion(char, str, pos):
	"""
	Inserts a character at a particular position into a particular string

		:param char: (string) the character to insert
		:param str: (string) the string to insert
		:param pos: (number) position to insert at

		:returns: (string) a string with *char* inserted at *pos*
	"""
	return str[0:pos] + char + str[pos:]

def recursive_string_permute(str):
	"""
	Recursively creates permutations of *str*

		:param str: (string) A string
		:returns: (string[]) A list of permuted strings of *str*

	Complexity::
		runtime O(n^2)
		space complexity O(n^2)
	"""
	if not str:
		return ['']

	currentChar = str[0]
	permutationList = []
	permutationOfRest = recursive_string_permute(str[1:])
	for permutedStr in permutationOfRest:
		for pos in range(len(permutedStr) + 1):
			permutationList.append(char_insertion(currentChar, permutedStr, pos))

	return permutationList

class Test(unittest.TestCase):
	def test_empty_string(self):
		self.assertListEqual([''], recursive_string_permute(''))

	def test_single_char(self):
		self.assertListEqual(['a'], recursive_string_permute('a'))

	def test_two_chars(self):
		self.assertSetEqual(
			set(['ab', 'ba']),
			set(recursive_string_permute('ab'))
		)

	def test_three_chars(self):
		self.assertCountEqual(
			['abc', 'bac', 'bca', 'cab', 'cba', 'acb'],
			recursive_string_permute('abc')
		)

	def test_four_chars(self):
		self.assertCountEqual(
			['abcd','acbd','abdc','adbc','adcb','acdb',
			 'bacd','bcad','bcda','badc','bdac','bdca',
			 'cadb','cdab','cdba','cbad','cbda','cabd',
			 'dabc','dbac','dbca','dcab','dcba','dacb'],
			 recursive_string_permute('abcd')
		)

unittest.main()