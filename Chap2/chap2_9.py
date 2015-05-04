#!/usr/bin/env python
# coding: utf-8

"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

from collections import Counter

def main():
    f_name = './hightemp.txt'
    f = open(f_name, 'r')
    lines = f.readlines()
    f.close()

    w_lst = [unicode(x.split('\t')[0], "utf-8") for x in lines]
    w_dic = Counter(w_lst)
    w_lst = [(v, k) for k, v in w_dic.iteritems()] # (Counter, word)
    w_lst.sort(reverse=True)

    for i in w_lst:
        print "%s (%d)" % (i[1], i[0])

    # $ cut -f 1 ./hightemp.txt | sort | uniq -c | sort -nr

if __name__ == "__main__":
    main()
