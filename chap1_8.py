#!/usr/bin/env python
# coding: utf-8

"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

import sys
import re


def cipher(lst):
    code = ""
    p = re.compile("[a-z]")
    for word in lst:
        for c in list(word):
            if re.match(p, c):
                code += chr(219 - ord(c))
            else:
                code += c
    return code
    
def main():
    print "Input text:"
    text = sys.stdin.readline()
    w_lst  = list(text.rstrip("\n"))
    code  = cipher(w_lst) # list -> str
    print "Text in cipher: %s" % (code)

if __name__ == "__main__":
    main()
