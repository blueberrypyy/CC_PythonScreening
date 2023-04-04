# This program is designed to find the total sum of even numbers in a given
# list. I have written two functions to complete the same task. The first 
# function utilizes Python built in methods as well as list comprehension
# to ensure the program is as efficient as it can be. 
# The second function utilizes a generator function to complete the same task.
# This generator function could be a better option when working with larger
# datasets as this method could help save on memory usage.

# Written by Justin Schadwill

# Create list of data
nums = list(range(11))

# Solution using list comprehension
def sum_of_evens(nums):
    answer = sum([num for num in nums if num % 2 == 0])
    return answer

print(sum_of_evens(list(range(11))))

# Solution using generator function
def even_numbers(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

ans = sum(even_numbers(nums))
print(ans)

    



