def find_longest_word(words):
    """Return longest word in list of words."""

    longest_word = ""

    for word in words:

        if len(word) > len(longest_word):

            longest_word = word

    return len(longest_word)




print(find_longest_word(["hi", "hello"])) # 5

print(find_longest_word(["Balloonicorn", "Hackbright"])) # 12