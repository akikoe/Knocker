#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""

import re

"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""
def tokenize_xml(path):
    name = ""
    name_lst = []
    lst = open(path, 'r').readlines()
    wp = re.compile(r"<word>(.*?)</word>")
    pp = re.compile(r"<NER>PERSON</NER>")
    for line in lst:
        wm = wp.match(line.lstrip())
        pm = pp.match(line.lstrip())
        if wm:
            name = wm.group(1)
        if pm:
            name_lst.append(name)
            name = ""
    return name_lst

def main():
    name_lst = tokenize_xml("./nlp.txt.xml")
    print ("\n".join(name_lst))
                            
if __name__ == '__main__':
    main()
