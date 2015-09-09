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
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""
def name_xml(tree):
    name_lst = []
    root = tree.getroot()
    for token in root.findall('.//token'):
        wrd = token.find('word').text
        if token.find('NER').text == "PERSON":
            sen = "{}".format(wrd)
            name_lst.append(sen)
    return name_lst

def main():
    tree = chap6_3.read_xml("./nlp.txt.xml")
    name_lst = name_xml(tree)
    print ("\n".join(name_lst))
                            
if __name__ == '__main__':
    main()
