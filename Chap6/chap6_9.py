#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""

from nltk.tree import Tree
import chap6_3
import re

"""
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
"""
def analyze_sexpression(tree):
    NP_lst = []
    root = tree.getroot()
    for parse in root.findall('.//parse'):
        t = Tree.fromstring(parse.text)
        height = t.height()
        for h in range(height):
            for s in t.subtrees(lambda t: t.height() == h):
                if "NP" == s.label(): NP_lst.append(str(s)) 
    return NP_lst

def main():
    tree = chap6_3.read_xml("./nlp.txt.xml")
    NP_lst = analyze_sexpression(tree)
    print ("\n".join(NP_lst))
    
if __name__ == '__main__':
    main()
