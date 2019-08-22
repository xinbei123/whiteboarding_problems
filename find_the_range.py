def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple."""

    if nums == []:

        return (None, None)

    min_num = min(nums)
    max_num = max(nums)

    return (min_num, max_num)

print(find_range([3, 4, 2, 5, 10]))
# (2, 10)

print(find_range([]))
# (None, None)

print(find_range([7]))
# (7, 7)

