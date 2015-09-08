#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""

import re

"""
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
"""

def split_sen(path):
    sen_lst = []
    lst = open(path, 'r').readlines()
    p = re.compile(u"([.;:?!])\s([A-Z])")
    for line in lst:
        sen_lst.extend(re.sub(p, r"\1\n\2", line.rstrip()).split("\n"))
    return sen_lst

def main():
    sen_lst = split_sen("./nlp.txt")
    print ("\n".join(sen_lst))

if __name__ == '__main__':
    main()
