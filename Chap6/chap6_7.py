#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""

import chap6_3
import re, pydot

"""
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

def convert_dotlang(tree):
    i = 0
    root = tree.getroot()
    for depend in root.findall('.//dependencies'):
        if depend.get('type') == "collapsed-dependencies":
            data = []
            for dep in depend.findall('dep'):
                g = dep.find('governor').text
                d = dep.find('dependent').text
                data.append((g, d))
            g = pydot.graph_from_edges(data)
            g.write_jpeg('./fig/sen{}.jpg'.format(i), prog='dot')
            i += 1

def main():
    tree = chap6_3.read_xml("./nlp.txt.xml")
    convert_dotlang(tree)

if __name__ == '__main__':
    main()
