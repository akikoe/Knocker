#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""

import chap6_3

"""
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

述語: nsubj関係とdobj関係の子（dependant）を持つ単語
主語: 述語からnsubj関係にある子（dependent）
目的語: 述語からdobj関係にある子（dependent）
"""
def ext_tuple(tree):
    sen_lst = []
    root = tree.getroot()
    for depend in root.findall('.//dependencies'):
        if depend.get('type') == "collapsed-dependencies":
            data = []
            nsubj, dobj = set(), set()
            for dep in depend.findall('dep'):
                if dep.get('type') == 'nsubj':
                    nsubj.add((dep.find('governor').text, dep.find('dependent').text))
                elif dep.get('type') == 'dobj':
                    dobj.add((dep.find('governor').text, dep.find('dependent').text))
            verb_lst = set()
            for i,j in list(nsubj):
                for k, l in list(dobj):
                    if i == k: sen_lst.append("{}\t{}\t{}".format(j, i, l))
    return sen_lst

def main():
    tree = chap6_3.read_xml("./nlp.txt.xml")
    sen_lst = ext_tuple(tree)
    print ("\n".join(sen_lst))

if __name__ == '__main__':
    main()
