def max_num(num_list):
    """Returns largest integer from given list"""

    maxed_num = num_list[0]

    for num in num_list:

        if num > maxed_num:

            maxed_num = num 
            
    return maxed_num





print(max_num([5, 3, 6, 2, 1])) # 6