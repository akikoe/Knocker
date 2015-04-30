#!/usr/bin/env python
# coding: utf-8

"""
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

import re

def match_word(p, word):
    w    = p.match(word)
    term = w.group()
    return term

def map_word(lst):
    dic     = dict() # dictionary type
    num_lst = [1, 5, 6, 7, 8, 9, 15, 16, 19] # 1-origin
    
    for i, j in enumerate(lst):
        if (i+1) in num_lst:
            num_lst.remove(i+1)
            dic[j[0]] = i # 0-origin
        else:
            dic[j[0:2]] = i
    return dic

def main():
    p = re.compile("[a-zA-Z].*[a-zA-Z]") # the longest matching
    text  = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    
    print "Text: ", text
    word_lst = [match_word(p, i) for i in text.split()] # Only Alphabet
    map_dic  = map_word(word_lst) # list -> dic
    print "Dictionary: ", map_dic

if __name__ == "__main__":
    main()
