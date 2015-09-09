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

def main():

if __name__ == '__main__':
    main()
