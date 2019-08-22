# >>> add_to_zero([])
# False

# >>> add_to_zero([1])
# False

# >>> add_to_zero([1, 2, 3])
# False

# >>> add_to_zero([1, 2, 3, -2])
# True

def add_to_zero(nums):
    """Given a list of ints, return True if any two nums sum to 0."""

    if nums == []:

        return False

    nums_set = set(nums)

    for num in nums_set:

        if -num in nums_set:

            return True

    return False


print(add_to_zero([])) # false
print(add_to_zero([1])) # false
print(add_to_zero([1, 2, 3])) #false
print(add_to_zero([1, 2, 3, -2])) #True