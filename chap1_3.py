#!/usr/bin/env python
# coding: utf-8

"""
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

import collections
import re

def is_alphabet(term):
    return re.match("[a-z]|[A-Z]", term)

def count(lst):
    count_lst = []
    
    n = len(lst)
    for i in range(n):
        term  = list(lst[i])
        c_dic = collections.Counter(term)
        c_lst = [(v, k) for k, v in c_dic.items()]
        c_lst.sort(reverse = True)
        count_lst.append([i[1] for i in c_lst if is_alphabet(i[1])])
    return count_lst

def main():
    text  = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

    print "Text: ", text
    word_lst = text.split()
    wc_lst = count(word_lst) # list -> list
    print "Count: ", wc_lst
        

if __name__ == "__main__":
    main()
