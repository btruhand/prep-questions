from math import ceil

# We have a list of integers, where:
# The integers are in the range 1..n
# The list has a length of n+1
# It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.
#
# Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)
#
# We're going to run this function on our new, super-hip MacBook Pro With Retina Display™. Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't upgrade our RAM. So we need to optimize for space!

# Complexity requirement: O(nlogn)
# Space requirement: O(1)

## algorithm explanation:
## find elements within the quadrants [low, center), [center, high]
## due to constraint of the question (duplicates ensured), one of the quadrants
## has to have higher amount of elements than the possible range of the quadrant
## quadrants are defined by the integer range not list size
def find_repeat(the_list):

    # Find a number that appears more than once
    low = 1
    high = len(the_list) - 1
    while low != high :
        center = low + ceil((high - low) / 2)
        num_less_than_center = 0

        for el in the_list:
            if el >= low and el < center:
                num_less_than_center += 1

        distinct_integers_possible_below_center = center - low
        if num_less_than_center > distinct_integers_possible_below_center:
            # duplicate must be in [low, center)
            high = center - 1
        else:
            # must be in the higher quadrant [center, high]
            low = center

    # low and high converged
    return low

print(find_repeat([3,1,3,2]))
print(find_repeat([1,1]))
print(find_repeat([7,6,3,5,7,7,4,2]))
print(find_repeat([1,4,3,3,5]))