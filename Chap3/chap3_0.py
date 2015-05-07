#!/usr/bin/env python
# coding: utf-8

"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json

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
        
if __name__ == "__main__":
    main()

