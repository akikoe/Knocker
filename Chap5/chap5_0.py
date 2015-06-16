#!/usr/bin/env python
# coding: utf-8

"""
前準備:
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
"""

import re

"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""
class Morph:
    def __init__(self, token):
        p = re.compile(u"<tok.*? feature=\"(.*?)\".*?>(.*?)<.tok>")
        m = p.match(token)
        self.surface = m.group(2) # 表層系
        m_lst = m.group(1).split(",")
        # tok/feature = 品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
        self.base = m_lst[6] # 基本形
        self.pos  = m_lst[0] # 品詞
        self.pos1 = m_lst[1] # 品詞細分類1
        
def read(path):
    lst = []
    
    f = open(path, "r")
    line = f.readline()

    p = re.compile(u"</sentence>")
    sen  = ""
    while line:
        line = line.rstrip()
        sen += line
        
        m = p.match(line)
        if m:
            lst.append(sen)
            sen = ""
        line = f.readline()    
    f.close()
    return lst

def make_morph(path):
    lst = read(path)
    
    morph_lst, m_lst = [], []
    p = re.compile(u"<tok id=.*?</tok>")
    for i in lst:
        token_lst = p.findall(i)
        for j in token_lst:
            m_lst.append(Morph(j))
        morph_lst.append(m_lst)
        m_lst = []
    return morph_lst

def show_morph(lst): # 3文目の形態素列を表示
    for i in lst[2]:
        print i.surface

        
def main():
    morph_lst = make_morph("./neko.txt.cabocha")
    show_morph(morph_lst)

if __name__ == "__main__":
    main()       
