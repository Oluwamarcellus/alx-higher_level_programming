#!/usr/bin/python3

det = 32
i = 122
while i >= 97:
    if det == 32:
        det = 0
    else:
        det = 32
    print("{}".format(chr(i - det)), end="")
    i -= 1
