#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""

import chap6_3

"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
"""

def coreference(tree):
    coref_lst = []
    root = tree.getroot()
    for corefer in root.findall('.//coreference'):
        for mention in corefer.findall('mention'):
            if mention.get('representative') == "true":
                rep_word = mention.find('text').text
            else:
                cor_word = mention.find('text').text
                coref_lst.append(rep_word + " ("+ cor_word + ")")
    return coref_lst

def main():
    tree = chap6_3.read_xml("./nlp.txt.xml")
    coref_lst = coreference(tree)
    print ("\n".join(coref_lst))

if __name__ == '__main__':
    main()
