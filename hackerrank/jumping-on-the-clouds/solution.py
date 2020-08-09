#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	# greedily find the answer to find minimal  jumps
	jump_counts = 0
	i = 0
	while i < len(c):
		lookahead = i + 2 
		if lookahead < len(c):
			if c[lookahead] == 0:
				i += 2
			else:
				# guaranteed that we have a path
				i += 1
		else:
			# guaranteed that we have a path
			i += 1
		jump_counts += 1
	# take off extra jump to reach the end of the list
	return jump_counts - 1

if __name__ == '__main__':
	fptr = os.environ.get('OUTPUT_PATH')
	if fptr is not None:
		fptr = open(os.environ['OUTPUT_PATH'], 'w')
	else:
		fptr = sys.stdout

	n = int(input())

	c = list(map(int, input().rstrip().split()))

	result = jumpingOnClouds(c)

	fptr.write(str(result) + '\n')

	fptr.close()
