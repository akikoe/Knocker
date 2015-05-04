#!/usr/bin/env python
# coding: utf-8

"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

import optparse

def main():
    # Parser Set
    parser = optparse.OptionParser()
    parser.add_option("-n", dest = "N", type = int, default = 1, help = "Let N (>0) lines show from the head.")
    options, args = parser.parse_args()

    f_name = './col1.txt'
    f = open(f_name, 'r')
    line = f.readline()
    i = 0 # counter
    
    while line:
        if i > options.N-1:
            print "---"
            i = 0
        print line.rstrip("\n")
        line = f.readline()
        i += 1
    f.close()

    # $ split -N ./col1.txt output

if __name__ == "__main__":
    main()
