def replace_vowels(chars):
    """Given list of chars, return a new copy, but with vowels replaced by '*'."""

    result = []

    for char in chars:

        if char in 'aeiouAEIOU':

            char = '*'

        result.append(char)

    return result


print(replace_vowels(['h', 'i']))
# ['h', '*']

print(replace_vowels(["A", "b"]))
# ['*', 'b']