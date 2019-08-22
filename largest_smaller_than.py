def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""

    if nums[0] > xnumber:

        return None

    if nums[-1] <  xnumber:

        return len(nums) -1

    for i, num in enumerate(nums):

        if num >= xnumber:

            return i-1
       




print(find_largest_smaller_than([-5, -2, 8, 12, 32], 10)) # 2
print(find_largest_smaller_than([-5, -2, 8, 12, 32], 33)) # 4
print(find_largest_smaller_than([-5, -2, 8, 12, 32], -1)) # 1
print(find_largest_smaller_than([-5, -2, 8, 12, 32], -10)) # None
