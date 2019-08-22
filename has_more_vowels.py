def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?"""

    v = {'a', 'e', 'i', 'o', 'u'}

    v_count = 0

    for letter in word:

        if letter.lower() in v:

            v_count += 1

    non_v_count = len(word) - v_count

    if v_count > non_v_count:

        return True

    else:

        return False





print(has_more_vowels("moose")) # True
print(has_more_vowels("mice")) # False
print(has_more_vowels("graph")) # False
print(has_more_vowels("yay")) # Fasle
print(has_more_vowels("Aal")) # True