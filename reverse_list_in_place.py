def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """
    result = []
    i = 0

    while i < len(lst):

        result.append(lst.pop())

    return result


print(rev_list_in_place([1, 2, 3])) # [3, 2, 1]