#!/usr/bin/env python
# coding: utf-8

"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

import subprocess

def main():
    file = './hightemp.txt'
    f    = open(file)
    line = f.readline()

    i = 0    
    while line:
        line = f.readline()
        i += 1
    print "Python counts: %d" % i 

    print "$ wc %s" % file
    subprocess.Popen(["wc", file], )
        
if __name__ == "__main__":
    main()
