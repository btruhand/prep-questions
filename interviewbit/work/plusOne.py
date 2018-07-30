from functools import reduce

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        idx = -1
        for digit in A:
            idx = idx + 1
            if digit != 0:
                break
        # slicing away to trim down the zeroes
        A = A[idx:]

        reversedA = list(reversed(A))
        addWith = 1
        for idx, digit in enumerate(reversedA):
            digit = digit + addWith
            if digit >= 10:
                digit = digit % 10
                addWith = 1
                reversedA[idx] = digit
            else:
                addWith = 0
                reversedA[idx] = digit
                break

        if addWith == 1:
          reversedA.append(1)
        return list(reversed(reversedA))

s = Solution()
print(s.plusOne([0,1,2]))
print(s.plusOne([9,9,9]))
print(s.plusOne([1,5,6,7,9,8,9]))
print(s.plusOne([0,1,5,8,9,9,0,9]))
