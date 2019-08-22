import random

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = []
    
    for i in range(n):

        num = random.choice(nums)
        nums.remove(num)
        result.append(num)

    return result



print(lucky_numbers(2))
# [3, 7]

print(lucky_numbers(0))
# []

print(lucky_numbers(10))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]