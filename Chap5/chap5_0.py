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

"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""
class Chunk:
    def __init__(self, tokens):
        m_lst = []
        p = re.compile(u"<tok id=.*?</tok>")
        token_lst = p.findall(tokens)
        for j in token_lst:
            m_lst.append(Morph(j))
        self.morphs = m_lst # 形態素(Morphオブジェクト)のリスト
                 
        p = re.compile(u"<chunk id=\"(.*?)\" link=\"(.*?)\".*?</chunk>")
        m = p.match(tokens)
        self.dst  = m.group(2)  # 係り先の文節インデックス番号
        self.scrs = [m.group(0)] # 係り元文節インデックス番号のリスト

def make_chunk(path):
    lst = read(path)
    
    chunk_lst, c_lst = [], []
    p = re.compile(u"<chunk id=.*?</chunk>")
    for i in lst:
        tokens_lst = p.findall(i)
        for j in tokens_lst:
            c_lst.append(Chunk(j))
        chunk_lst.append(c_lst)
        c_lst = []
    return chunk_lst


def show_chunk(lst): # 8文目の文節の文字列と係り先を表示
    for i in lst[7]:
        moji = ""
        for j in i.morphs:
            moji += j.surface
        print moji, i.dst
        
def main():
    # Chap5_0
    morph_lst = make_morph("./neko.txt.cabocha")
    show_morph(morph_lst)

    # Chap5_1
    chunk_lst = make_chunk("./neko.txt.cabocha")
    show_chunk(chunk_lst)
    
if __name__ == "__main__":
    main()       
