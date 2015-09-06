#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""
import chap6_0, chap6_1
from stemming.porter import stem # Porter's stemmer work only with Python2.7

"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""

def stemming(lst):
    stem_lst = []
    for wrd in lst:
        stem_lst.append(wrd + "\t" + stem(wrd))
    return stem_lst
    
def main():
    sen_lst = chap6_0.split_sen("./nlp.txt")
    wrd_lst = chap6_1.tokenize(sen_lst)
    stem_lst = stemming(wrd_lst)
    print ("\n".join(stem_lst))

if __name__ == '__main__':
    main()
