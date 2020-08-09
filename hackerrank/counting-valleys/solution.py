import math
import os
import random
import re
import sys

DOWNHILL = 'D'
UPHILL = 'U'

def countingValleys(n, s):
	elevation = 0
	valley_counts = 0
	for direction in s:
		is_came_down = False
		if direction == UPHILL:
			is_came_down = False
			elevation += 1
		else:
			is_came_down = True
			elevation -= 1
		
		if elevation == 0 and not is_came_down:
			valley_counts += 1
	
	return valley_counts


if __name__ == '__main__':
	fptr = os.environ.get('OUTPUT_PATH')
	if fptr is not None:
		fptr = open(os.environ['OUTPUT_PATH'], 'w')
	else:
		fptr = sys.stdout
	n = int(input())
	s = input()
	result = countingValleys(n, s)
	fptr.write(str(result) + '\n')
	fptr.close()