def is_palindrome(word):
    """Return True/False if this word is a palindrome."""

    word_reversed = word[::-1]

    if word == word_reversed:

        return True

    else:

        return False




print(is_palindrome("a")) # True
print(is_palindrome("noon")) # True
print(is_palindrome("racecar")) # True
print(is_palindrome("porcupine")) # False
print(is_palindrome("Racecar")) # False


