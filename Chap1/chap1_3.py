#!/usr/bin/env python
# coding: utf-8

"""
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

import collections
import re

def main():
    text  = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

    print "Text: ", text
    word_lst = text.split()
    wc_lst = [len(i) for i in word_lst if i.isalpha()] # list -> list
    print "Count: ", wc_lst
        

if __name__ == "__main__":
    main()
