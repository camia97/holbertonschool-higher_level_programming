#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == 0:
        sentence[0] = None
        return (0, None)
    a = (len(sentence), sentence[0])
    return a
