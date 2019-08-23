def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    result = set()
    print(result)

    for char in sentence:

        if char.lower().isalpha():

            result.add(char.lower())

    print(set(result))

    if len(result) == 26:

        return True

    else:

        return False




print(is_pangram("The quick brown fox jumps over the lazy dog!")) # True
print(is_pangram("I like cats, but not mice")) # False

# split the sentence into a list of chars (turn into set)
# loop over to see if word is in a-z