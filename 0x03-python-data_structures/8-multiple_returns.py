#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_l = len(sentence)
    if (sentence_l == 0):
        new_tuple = (sentence_l, None)
    else:
        new_tuple = (sentence_l, sentence[0])
    return (new_tuple)
