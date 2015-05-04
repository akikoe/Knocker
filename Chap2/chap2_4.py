#!/usr/bin/env python
# coding: utf-8

"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

import optparse

def main():
    # Parser Set
    parser = optparse.OptionParser()
    parser.add_option("-n", dest = "N", type = int, default = 1, help = "Let N lines show from the head.")
    options, args = parser.parse_args()

    f_name = './col1.txt'
    f = open(f_name, 'r')

    for i in range(options.N):
        line = f.readline()
        print line.rstrip("\n")
    f.close()

    # $ head -N ./col1.txt 

if __name__ == "__main__":
    main()
