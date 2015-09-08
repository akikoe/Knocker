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
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

def convert_dotlang(tree):
    data = "digraph sample {\n"
    coref_lst = []
    root = tree.getroot()
    for depend in root.findall('.//dependencies'):
        if depend.get('type') == "collapsed-dependencies":
            for dep in depend.findall('dep'):
                g = dep.find('governor').text
                d = dep.find('dependent').text
                data += "{} -> {};\n".format(g, d)
        else:
            data += "}\ndigraph sample {\n" # はじまり
    open("./token.dot", "w").write(data) # DOT言語作成
    
"""
    画像に変換
    $ dot -Tpng token.dot -o token.png                                       
"""

def main():
    tree = chap6_3.read_xml("./nlp.txt.xml")
    convert_dotlang(tree)

if __name__ == '__main__':
    main()
