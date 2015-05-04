#!/usr/bin/env python
# coding: utf-8

"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""

def main():
    f_name = './col1.txt'
    f = open(f_name, 'r')
    line = unicode(f.readline(), "utf-8")
    set_line = set()
    
    while line:
        set_line.add(line)
        line = unicode(f.readline(), "utf-8")
    f.close()
    print len(set_line)

    # $ sort col1.txt| uniq | wc

if __name__ == "__main__":
    main()
