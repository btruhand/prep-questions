from functools import reduce

def getMinimumDistance(fPoint, sPoint):
	return max(abs(fPoint[0] - sPoint[0]), abs(fPoint[1] - sPoint[1]))

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
		pointsAB = tuple(zip(A, B))
		accumulation = reduce(lambda acc, el: [acc[0] + getMinimumDistance(acc[1], el), el], pointsAB, [0, pointsAB[0]])
		return accumulation[0]

s = Solution()
print(s.coverPoints([1,2,6],[1,4,2]))
print(s.coverPoints([-2],[7]))
print(s.coverPoints([-1,0,1],[-2,3,-4]))