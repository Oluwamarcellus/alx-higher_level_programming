#!/usr/bin/python3
"""
5-text_indentation Module
prints a text with 2 new lines after each of these characters: ., ? and :

"""


def text_indentation(text):
    """prints a text with 2 new lines after
    ('.', '?', ':')
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in ".?:":
        text = f"{char}\n\n".join([i.strip(" ") for i in text.split(char)])

    print(text, end="")
