#!/usr/bin/python3
"""
this module is used for text formating
"""


def text_indentation(text):
    """ function that prints a text with 2 new lines after each of these
    characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    spe_char = ['.', '?', ':']
    formated_text = ""
    i = 0
    while i < len(text):
        if not text[i] in spe_char:
            formated_text += text[i]
        else:
            formated_text += text[i]
            formated_text += 2 * "\n"
            while text[i + 1] == " ":
                i += 1
        i += 1
    print(formated_text, end='')
