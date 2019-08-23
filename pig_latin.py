def pig_latin(phrase):
    """Turn a phrase into pig latin."""


    # loop over each word in the phrase
    # in word[0] starts with aeiou
    # add yay to the end of that word
    # if word[0] starts with non aeiou
    # move word[0] to the end and add ay

    result = []

    for word in phrase.split():

        if word[0] in 'aeiou':

            result.append(word + 'yay')

        else:

            result.append(word[1:] + word[0] + 'ay')

    return " ".join(result)

    


print(pig_latin('porcupines are cute'))
#'orcupinespay areyay utecay'

print(pig_latin('give me an apple'))
#'ivegay emay anyay appleyay'


# If the word begins with a consonant (not a, e, i, o, u), 
# move the first letter to the end and add ‘ay’
# If the word begins with a vowel, add ‘yay’ to the end
