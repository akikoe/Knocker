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
    lst = []
    for i in sen_lst:
        m = p.search(i)
        if m:
            print m.group()
            lst.append(m.group())
    return lst

"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""
def ExtCateNameOfEn(lst):
    p  = re.compile(":.*?]")
    for i in lst:
        m = p.search(i)
        if m:
            print m.group().lstrip(":").rstrip("]")

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""
def SectStruct(data):
    p = re.compile("==.+==")
    sen_lst = data["text"].split("\n")
    for i in sen_lst:
        m = p.search(i)
        if m:
            moji  = m.group()
            count =  (moji.count("=")/2) -1
            print moji.replace("=", ""), count
            
            
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
    cate_lst = ExtSenOfEnCate(data) # Chap3-1

    print "\n(3-2):"
    ExtCateNameOfEn(cate_lst)

    print "\n(3-3):"
    SectStruct(data)
    
if __name__ == "__main__":
    main()

