#!/usr/bin/env python
# coding: utf-8

"""
2. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

def main():
    file  = './hightemp.txt'
    file2 = './col1.txt'
    file3 = './col2.txt'
    f    = open(file, 'r')
    f2   = open(file2, 'w')
    f3   = open(file3, 'w')
    line = f.readline()

    i = 0    
    while line:
        text = unicode(line, "utf-8").split("\t")
        f2.writelines(text[0].encode("utf-8") +"\n")
        f3.write(text[1].encode("utf-8") +"\n")
        line = f.readline()
    f.close()
    f2.close()
    f3.close()

    # $ cut -f 1 ./hightemp.txt > col1.txt
    # $ cut -f 2 ./hightemp.txt > col2.txt

if __name__ == "__main__":
    main()
