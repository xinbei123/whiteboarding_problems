def show_evens(nums):
    """Given list of ints, 
    return list of *indices* of even numbers in list."""

    result = []

    for i, num in enumerate(nums):

        if num % 2 == 0:

            result.append(i)

    return result



print(show_evens([1, 2, 3, 4, 6, 8]))
# [1, 3, 4, 5]