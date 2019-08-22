def max_of_three(num1, num2, num3):
    """Returns the largest of three integers"""

    if num1 >= num2 and num1 >= num3:

        return num1

    elif num2 >= num1 and num2 >= num3:

        return num2

    elif num3 >= num1 and num3 >= num2:

        return num3




print(max_of_three(1, 5, 2)) # 5

print(max_of_three(10, 1, 11)) # 11