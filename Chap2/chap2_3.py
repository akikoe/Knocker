#!/usr/bin/env python
# coding: utf-8

"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""

def main():
    file1 = './col1.txt'
    file2 = './col2.txt'
    file3 = './merge.txt'
    f    = open(file1, 'r')
    f2   = open(file2, 'r')
    f3   = open(file3, 'w')
    lines1 = f.readlines()
    lines2 = f2.readlines()

    for i, j in zip(lines1, lines2):
        f3.writelines(i.rstrip("\n") +"\t" +j)
    f.close()
    f2.close()
    f3.close()

    # $ $ paste -d "\t" col1.txt col2.txt > merge.txt

if __name__ == "__main__":
    main()
