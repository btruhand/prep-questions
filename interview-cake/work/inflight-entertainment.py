from typing import List
import unittest

def inflight_entertainment(flight_length: int, movie_lengths: List[int]) -> bool:
	"""Inflight Entertainment

	Please see `problem description <https://www.interviewcake.com/question/python/inflight-entertainment>`_

	:param flight_length: Duration of flight
	:type flight_length: int
	:param movie_lengths: Duration of movies
	:type movie_lengths: List[int]
	:return: True if there are two movies whose length equals the flight_length
	:rtype: bool
	"""
	pair_up_dictionary = set()
	for movie_duration in movie_lengths:
		remaining_duration = flight_length - movie_duration
		if remaining_duration not in pair_up_dictionary:
			pair_up_dictionary.add(movie_duration)
		else:
			return True

	return False

class TestInflightEntertainment(unittest.TestCase):
	def test_no_movies_at_all(self):
		self.assertFalse(inflight_entertainment(100, []))

	def test_only_one_movie(self):
		self.assertFalse(inflight_entertainment(10, [1]))

	def test_one_movie_that_equates_flight_length(self):
		self.assertFalse(inflight_entertainment(2, [2]))

	def test_two_movies_that_equate_flight_length(self):
		self.assertTrue(inflight_entertainment(80, [20, 50, 10, 40, 60, 90]))

	def test_movies_with_same_length(self):
		self.assertTrue(inflight_entertainment(90, [30, 50, 70, 100, 45, 45]))

	def test_sinlge_movie_with_half_duration_of_flight(self):
		self.assertFalse(inflight_entertainment(90, [30, 50, 70, 100, 45, 55]))


unittest.main()