def is_prime(num):
    """Is a number a prime number?"""

    if num == 0 or num == 1:

        return False
    else:

        if num % 2 != 0:

            return True

        else:

            return False




print(is_prime(0)) # False
print(is_prime(1)) # False
print(is_prime(3)) # True
print(is_prime(4)) # False