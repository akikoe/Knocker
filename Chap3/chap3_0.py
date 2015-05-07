#!/usr/bin/env python
# coding: utf-8

"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json
import re

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""
def ExtSenOfEnCate(data):
    p = re.compile(".*Category.*")
    sen_lst = data["text"].split("\n")
    for i in sen_lst:
        m = p.search(i)
        if m:
            print m.group()

def main():
    f_path = './jawiki-country.json'
    f = open(f_path, 'r')
    line = f.readline()

    while line:
        data = json.loads(line)
        if data["title"] == u"イギリス":
            print data["text"] # Chap3-0
            break
        line = f.readline()

    print "\n(3-1):"
    ExtSenOfEnCate(data) # Chap3-1

if __name__ == "__main__":
    main()

