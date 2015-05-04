#!/usr/bin/env python
# coding: utf-8

"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import optparse

def main():
    # Parser Set
    parser = optparse.OptionParser()
    parser.add_option("-n", dest = "N", type = int, default = 1, help = "Let N lines show from the end.")
    options, args = parser.parse_args()

    f_name = './col1.txt'
    f = open(f_name, 'r')
    lines = f.readlines()
    n = len(lines)
    
    for i in range(options.N)[::-1]:
        print lines[(n-1)-i].rstrip("\n")
    f.close()

    # $ tail -N ./col1.txt 

if __name__ == "__main__":
    main()
