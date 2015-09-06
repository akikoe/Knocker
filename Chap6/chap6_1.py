#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""

import chap6_0

"""
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ
"""

def tokenize(lst):
    sen_lst = [line.split(" ") for line in lst]
    wrd_lst = []
    for line in sen_lst:
        wrd_lst.extend(line + [""])
    return wrd_lst
    
def main():
    sen_lst = chap6_0.split_sen("./nlp.txt")
    wrd_lst = tokenize(sen_lst)
    print ("\n".join(wrd_lst))
    
if __name__ == '__main__':
    main()
