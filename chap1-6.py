#!/usr/bin/env python
# coding: utf-8

"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

"""
import chap1_5 as c15

def in_lst(bigram, xset):
    if (bigram[0], bigram[1]) in xset: return True
    else: return False

def get_sets(lst, lst2):
    moji = 'se'
    
    X, Y = set(lst), set(lst2)
    print "set X: ", X
    print "set Y: ", Y
    print "wa-set: "  , X.union(Y)        # X | Y
    print "seki-set: ", X.intersection(Y) # X & Y
    print "sa-set: "  , X.difference(Y)   # X - Y
    print "Check if %s in X: %s " % (moji, in_lst(moji, X))
    print "Check if %s in Y: %s " % (moji, in_lst(moji, Y))
    
def main():
    text  = "paraparaparadise"
    text2 = "paragraph"
    
    print "Text1: %s\nText2: %s" % (text, text2)
    c_lst  = list(text)
    c2_lst = list(text2)
    c_bigram  = c15.n_gram(2, c_lst) # list -> pair list
    c2_bigram = c15.n_gram(2, c2_lst)
    get_sets(c_bigram, c2_bigram)

if __name__ == "__main__":
    main()
