from typing import List
import unittest

def find_rotation_point(words: List[str]) -> int:
	"""Finding index point where words start alphabetically

	Given a list of words that is almost fully sorted, find the index of the list
	where the words start to be "rotated" (the word that should have been at the beginning
	of the list had it been fully sorted)

	.. note::
		Please check out the <problem description `https://www.interviewcake.com/question/python/find-rotation-point`>_

	:param words: List of words almost fully sorted
	:type words: List[str]
	:return: Index point where words are rotated
	:rtype: int
	"""

	low = 0
	high = len(words) - 1
	check_against = words[0]

	while low < high - 1:
		midpoint = (high + low) // 2
		if check_against < words[midpoint]:
			# then this must be that we want to go to the right side
			# since rotation point is to the right
			low = midpoint
		elif check_against > words[midpoint]:
			# then this must be that we want to go to the left side
			# in order to close down the gap to the rotation point
			high = midpoint
		check_against = words[midpoint]

	# checks if list is actually rotated
	if words[0] > words[high]:
		# high must be the rotation point now since we've pinpointed it
		return high
	else:
		# beginning of list is lower than what is presumed to be rotation point
		# so there must not be any rotation point
		return 0

class TestFindRotationPoint(unittest.TestCase):
	def test_sample_input(self):
		self.assertEqual(5, find_rotation_point([
			'ptolemaic',
			'retrograde',
			'supplant',
			'undulate',
			'xenoepist',
			'asymptote',  # <-- rotates here!
			'babka',
			'banoffee',
			'engender',
			'karpatka',
			'othellolagkage'
		]))

	def test_rotation_is_after_mid_point(self):
		self.assertEqual(3, find_rotation_point([
			'test',
			'unbradled',
			'wyoming',
			'active',
			'best'
		]))

	def test_rotation_is_before_mid_point(self):
		self.assertEqual(2, find_rotation_point([
			'hey',
			'man',
			'assert',
			'best',
			'celestial',
			'draph'
		]))

	def test_rotation_point_is_at_end_of_list(self):
		self.assertEqual(6, find_rotation_point([
			'blades',
			'counter',
			'master',
			'xenophobia',
			'yngwie',
			'zebra',
			'assertion'
		]))

	def test_single_entry(self):
		self.assertEqual(0, find_rotation_point(['entry']))

unittest.main()