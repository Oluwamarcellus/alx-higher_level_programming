#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    ret = None
    try:
        ret = fct(*args)
    except Exception as all:
        print("Exception: {}".format(all), file=sys.stderr)
    finally:
        return ret
