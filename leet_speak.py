def translate_leet(phrase):
    """Translates input into "leet-speak"."""

    to_leet_dict = {'a': '@', 'o': '0', 'e': '3', 'l': '1', 's': '5', 't': '7'}

    result = ""

    for char in phrase:

        if char not in to_leet_dict.keys():

            result += char

        else:

            result += to_leet_dict[char]

    return result


print(translate_leet("Hi Balloonicorn"))
# 'Hi B@1100nic0rn'

print(translate_leet("Hackbright is the Shizzle"))
# 'H@ckbrigh7 i5 7h3 5hizz13'