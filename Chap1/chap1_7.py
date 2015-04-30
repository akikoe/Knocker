#!/usr/bin/env python
# coding: utf-8

"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""

def generate_sen(x, y, z):
    text = "%d時の%sは%.1f" % (x, y, z)
    return text

def main():
    x = 12
    y = "気温"
    z = 22.4
    
    text = generate_sen(x, y, z)
    print text
    
if __name__ == "__main__":
    main()
