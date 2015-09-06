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

def output_line(path):
    lst = open(path, 'r').readlines()
    p = re.compile(u"[.;:?!]\s[A-Z]")
    for line in lst:
        if p.search(line):
            replace_lst = p.findall(line)
            replace_lst = [i.replace(" ", "\n") for i in replace_lst] + [""]
            line = p.split(line.rstrip())
            print ("".join([i+j for i, j in zip(line, replace_lst)]))
        else:
            print (line.rstrip())

def main():
    output_line("./nlp.txt")

if __name__ == '__main__':
    main()
