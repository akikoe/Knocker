#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""
import re

"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．

"""

def tokenize_xml(path):
    wrd_line = ""
    wrd_lst = []
    lst = open(path, 'r').readlines()
    wp = re.compile(r"<word>(.*?)</word>")
    lp = re.compile(r"<lemma>(.*?)</lemma>")
    pp = re.compile(r"<POS>(.*?)</POS>")
    for line in lst:
        wm = wp.match(line.lstrip())
        lm = lp.match(line.lstrip())
        pm = pp.match(line.lstrip())
        if wm:
            wrd_line += wm.group(1)
        elif lm:
            wrd_line += "\t" + lm.group(1)
        elif pm:
            wrd_line += "\t" + pm.group(1)
            wrd_lst.append(wrd_line)
            wrd_line = ""
    return wrd_lst

def main():
    wrd_lst = tokenize_xml("./nlp.txt.xml")
    print ("\n".join(wrd_lst))

if __name__ == '__main__':
    main()
