#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""

import chap6_3
import re

"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．

"""

def tokenize_xml(tree):
    wrd_lst = []
    root = tree.getroot()
    for token in root.findall('.//token'):
        wrd = token.find('word').text
        lem = token.find('lemma').text
        pos = token.find('POS').text
        sen = "{}\t{}\t{}".format(wrd, lem, pos)
        wrd_lst.append(sen)
    return wrd_lst

def main():
    tree = chap6_3.read_xml("./nlp.txt.xml")
    wrd_lst = tokenize_xml(tree)
    print ("\n".join(wrd_lst))

if __name__ == '__main__':
    main()
