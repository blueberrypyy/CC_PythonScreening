# This program is designed to find the largest sum of any and all contiguous 
# subarrays of the original list. The first function will iterate through the list
# while keeping track of the current subarray sum. The function will remember
# the largest sum so far and save it to memory. If the sum is negative, the 
# function will reset the current sum to 0 because a negative number will only
# decrease the sum.

# I used a built in Python contant ('-inf') as an initial value of negative infinity
#to max_sum. This will ensure any positive value in the list will be greater than the initial value.

# I then implemented a generator function to generate all contiguous subarrays
# of the original list. This function is not necessary and is only helpful if 
# you are dealing with a much larger dataset. 

# Create list of data
nums = [1, -2, 3, 4, -5, 6]

# Original solution
def sum_max_contiguous(nums):
    max_sum = float('-inf') 
    curr_sum = 0

    for num in nums:
        curr_sum += num 
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum

print(sum_max_contiguous(nums))

# Extra generator function
def sum_max_generator(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            yield sum_max_contiguous(nums[i: j])

#for max_sum in sum_max_generator(nums):
#    print(max_sum)


