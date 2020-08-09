#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY x
#

def maxMin(operations, x):
	# Write your code here
	result = []
	elements = []

	maxVal = -math.inf
	minVal = math.inf
	for idx, op in enumerate(operations):
		if op == "push":
			elements.append(x[idx])
			maxVal = max(maxVal, x[idx])
			minVal = min(minVal, x[idx])
		else:
			# do something for pop
			elements.remove(x[idx])
			maxVal = max(-math.inf, *elements)
			minVal = min(math.inf, *elements)
		
		result.append(maxVal * minVal)
	return result

if __name__ == '__main__':
	if os.environ.get('OUTPUT_PATH') is not None:
		fptr = open(os.environ['OUTPUT_PATH'], 'w')
	else:
		fptr = sys.stdout

	operations_count = int(input().strip())

	operations = []

	for _ in range(operations_count):
		operations_item = input()
		operations.append(operations_item)

	x_count = int(input().strip())

	x = []

	for _ in range(x_count):
		x_item = int(input().strip())
		x.append(x_item)

	result = maxMin(operations, x)

	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
