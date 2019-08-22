def concat_lists(list1, list2):
    """Combine lists."""
    for num in list2:
        list1.append(num)

    return list1



print(concat_lists([1,2], [3,4])) 
# [1, 2, 3, 4]

print(concat_lists([], [3,4])) 
# [3, 4]

print(concat_lists([1,2], [])) 
# [1, 2]

print(concat_lists([], [])) 
#[]