#!/usr/bin/env python
# coding: utf-8

"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

def main():
    f_name = './hightemp.txt'
    f = open(f_name, 'r')
    line = unicode(f.readline(), "utf-8")
    lst = []
    
    while line:
        lst.append((line.split('\t')[2], line.strip("\n")))
        line = unicode(f.readline(), "utf-8")
    f.close()

    lst.sort(reverse = True)
    for i in lst:
        print i[1]

    # $ sort -k 3 -r hightemp.txt

if __name__ == "__main__":
    main()
