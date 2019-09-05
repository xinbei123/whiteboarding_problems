def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""

    temp = variable_name.split()

    result = []

    for i, char in enumerate(temp):

        if char == '_':

            temp[i+1] = char.upper()

            result.append(char)

    return result

        




print(snake_to_camel("hi_balloonicorn"))
# 'hiBalloonicorn'