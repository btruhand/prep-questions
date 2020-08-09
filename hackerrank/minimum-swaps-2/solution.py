#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# def minimumSwaps(arr):
# 	swaps_needed = 0
# 	track_location_and_values = {}

# 	for idx, val in enumerate(arr):
# 		track_location_and_values[val] = idx
# 		if val - 1 != idx:
# 			# basically since the values are between 1 to n
# 			# then we know the minimum swap needed is just to
# 			# swap to the correct index everytime (direct assignment)
# 			swaps_needed += 1
# 			# track_location_and_values[val] = idx

# 			if arr[val - 1] - 1 == idx:
# 				location_of_pair = track_location_and_values.get(arr[val - 1])
# 				if location_of_pair == val - 1:
# 					# thinking about it there may be values, y, that
# 					# are in the slot that the current value, x, holds and that
# 					# the correct location of y is the current location of x
# 					# hence the optimal choice is to swap x and y's location because
# 					# we can save one more swap that way
# 					# since we can check this both ways (at the front and at the back),
# 					# we have this tracking of location and value
# 					swaps_needed -= 1

# 	# we return minus 1 because the last swap is placing
# 	# two values at the correct spot simultaneously
# 	return swaps_needed - 1

def minimumSwaps(arr):
	idx = 0
	swaps_needed = 0
	while idx != len(arr):
		if arr[idx] != idx + 1:
			temp = arr[arr[idx] - 1]
			arr[arr[idx] - 1] = arr[idx]
			arr[idx] = temp
			swaps_needed += 1
		else:
			idx += 1
	return swaps_needed

if __name__ == '__main__':
	if os.environ.get('OUTPUT_PATH') is None:
		fptr = sys.stdout
	else:
		fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	res = minimumSwaps(arr)

	fptr.write(str(res) + '\n')

	fptr.close()