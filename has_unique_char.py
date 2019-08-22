def has_unique_chars(word):
    """Does word contains unique set of characters?"""

    new_word = set(word)

    if len(new_word) == len(word):

        return True

    else:

        return False





print(has_unique_chars("Monday")) # True
print(has_unique_chars("Moonday")) # False
print(has_unique_chars("")) # True

# turn the string to a set of characters
# and turn back to a string
# if len(1st string) is eqal to len(2nd string)
# return true