#!/usr/bin/env python
# coding: utf-8

"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

import random

def scrumble(lst):
    sen = ""
    
    for i in lst:
        n     = len(i)
        if n < 5:
            sen += i
        else:
            i_lst = list(i)
            ii_lst = i_lst[1:n-1]
            random.shuffle(ii_lst)
            sen += i[0] + "".join(ii_lst) + i[n-1]
        sen += " "
    return sen.rstrip(" ")

def main():
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    print "Text: %s" % (text)
    w_lst = text.split()
    sen   = scrumble(w_lst) # list -> str
    print "Scrumbled Text: %s" % (sen)

if __name__ == "__main__":
    main()
