#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""

import re

"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
"""

def coreference(path):
    cor_word = ""
    coref_lst = []
    lst = open(path, 'r').readlines()
    rp = re.compile(r"<mention representative=\"true\">")
    tp = re.compile(r"<text>(.*?)</text>")
    for line in lst:
        rm = rp.match(line.lstrip())
        tm = tp.match(line.lstrip())
        if rm:
            rep_word = ""
        if tm:
            if rep_word:
                cor_word = tm.group(1)
                coref_lst.append(rep_word + " ("+ cor_word + ")")
            else:
                rep_word = tm.group(1)
    return coref_lst

def main():
    coref_lst = coreference("./nlp.txt.xml")
    print ("\n".join(coref_lst))

if __name__ == '__main__':
    main()
