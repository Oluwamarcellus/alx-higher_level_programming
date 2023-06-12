#!/usr/bin/python3
def multiple_returns(sentence):
    if isinstance(sentence, str):
        return(len(sentence), None if not sentence else sentence[0])
