class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxSubArray(self, A):
		currentAccumulated = A[0]
		currentGreatest = currentAccumulated
		for el in A[1:]:
			addedValue = currentAccumulated + el
			# to handle the case where coming from a negative currentAccumulated value
			if el >= addedValue:
				currentAccumulated = el
			# if addedValue goes negative then there is no need to continue 
			elif addedValue >= 0:
				currentAccumulated = addedValue
			# anything else (which means that addedValue was negative), then just use current value
			else:
				currentAccumulated = el

			if currentGreatest <= currentAccumulated:
				currentGreatest = currentAccumulated

		return currentGreatest

s = Solution()
print(s.maxSubArray([0]))
print(s.maxSubArray([1,2]))
print(s.maxSubArray([-2,0]))
print(s.maxSubArray([-1]))
print(s.maxSubArray([-1,2,-2,5,-3]))
print(s.maxSubArray([-120,-202,-293,-60,-261,-67,10]))
print(s.maxSubArray([-120,120,-140]))
print(s.maxSubArray([-120,130,150,-300]))
print(s.maxSubArray([150,-120,-40,160,10]))
print(s.maxSubArray([150,-120,-20,160,10]))