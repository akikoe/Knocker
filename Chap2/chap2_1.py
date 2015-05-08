#!/usr/bin/env python
# coding: utf-8

"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

def main():
    file = './hightemp.txt'
    f    = open(file, 'r')
    doc  = []
    line = f.readline()

    while line:
        doc.append(line.replace("\t", " "))
        line = f.readline()
    f.close()
    print "Python does: %s" % "".join(doc)

    # $ sed $'s/\t/ /g ./hightemp.txt

if __name__ == "__main__":
    main()
