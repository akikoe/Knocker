#!/usr/bin/env python
# coding: utf-8

"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

from itertools import chain
import sys

def n_gram(n, seq):
    n_gram = []

    m = len(seq)
    for i in range(m-n+1):
        pair = ()
        for j in range(n):
            pair += (seq[i+j],)
        n_gram.append(pair)
    return n_gram

def main():
    text  = "I am an NLPer"
    
    print "Text: ", text
    word_lst = text.split()
    char_lst = list(chain.from_iterable(word_lst))
    c_bigram = n_gram(2, char_lst) # list -> pair list
    w_bigram = n_gram(2, word_lst)
    print "Character-based n_gram: ", c_bigram
    print "Word-based n_gram: ", w_bigram

if __name__ == "__main__":
    main()
