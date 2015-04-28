#!/usr/bin/env python
# coding: utf-8

"""
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

def concatenate(lst):
    word = ""

    n = len(lst)/2
    for i in range(n):
        j = 2*i +1
        word += lst[j]
        print lst[j]
    return word

def main():
    mojis = "パタトクカシーー"

    print "before:", mojis
    u_mojis  = unicode(mojis, "utf-8")  # -> unicode
    moji_lst = list(u_mojis)     # string -> list
    word_lst = concatenate(moji_lst)
    words    = "".join(word_lst) # list -> string
    print "after: ", words
    
if __name__ == "__main__":
    main()
