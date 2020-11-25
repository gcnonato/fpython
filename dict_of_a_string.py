"""Creates a dictionary from a given string"""


def string_to_dict(s):
    """Prints a list from a sorted string

    >>> string_to_dict('banana')
    {'a': 3, 'b': 1, 'n': 2}
    >>> string_to_dict('bandeira do brasil')
    {' ': 2, 'a': 3, 'b': 2, 'd': 2, 'e': 1, 'i': 2, 'l': 1, 'n': 1, 'o': 1, 'r': 2, 's': 1}

    :param s: string
    """

    string_dict = {}
    sorted_string = sorted(s)
    last_character = sorted_string[0]
    count = 1

    for character in sorted_string[1:]:
        if character == last_character:
            count += 1
        else:
            string_dict[last_character] = count
            last_character = character
            count = 1

    string_dict[last_character] = count

    return string_dict
