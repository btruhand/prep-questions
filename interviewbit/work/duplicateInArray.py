# Problem: https://www.interviewbit.com/problems/find-duplicate-in-array/

class Solution:
	def goToNextLocation(self, A, currentLocation):
		return A[currentLocation - 1]

	# @param A : tuple of integers
	# @return an integer
	def repeatedNumber(self, A):
		location = 0
		for _ in range(len(A) - 1):
			location = self.goToNextLocation(A, location)

		cycleLength = 1
		currentLocation = self.goToNextLocation(A, location)
		while location != currentLocation:
			cycleLength = cycleLength + 1
			currentLocation = self.goToNextLocation(A, currentLocation)
		
		locationOne = 0
		locationTwo = 0
		for _ in range(cycleLength):
			locationTwo = self.goToNextLocation(A, locationTwo)
		
		while locationOne != locationTwo:
			locationOne = self.goToNextLocation(A, locationOne)
			locationTwo = self.goToNextLocation(A, locationTwo)
		
		return locationOne

s = Solution()
print(s.repeatedNumber([1,2,3,2])) # 2 -> 2 -> 2
print(s.repeatedNumber([4,3,1,5,6,7,2,2])) # 2 -> 3 -> 1 -> 4 -> 5 -> 6 -> 7
print(s.repeatedNumber([1,6,5,1,4,3,2])) # 6 -> 3 -> 5 -> 4 -> 1 -> 1