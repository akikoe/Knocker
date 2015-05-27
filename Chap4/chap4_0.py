#!/usr/bin/env python
# coding: utf-8

"""
前準備:
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ
-> $ cat neko.txt | mecab >& neko.txt.mecab

なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．
"""

import sys
import re

"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""
def MakeMorphoDic(path):
    m_dic_lst   = []
    
    f = open(path, "r")
    line = f.readline()
    p = re.compile(u"(.*?)\t(.*?)\n")
    while line:
        m_dic = {}
        m = p.match(line)
        if m:
            #Memo: 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
            m_dic["surf"] = m.group(1) # 表層形
            feat_lst = m.group(2).split(',')
            m_dic["base"] = feat_lst[6]
            m_dic["pos"]  = feat_lst[0]
            m_dic["pos1"] = feat_lst[1]
            m_dic_lst.append(m_dic)
        line = f.readline()    
    f.close()
    return m_dic_lst

"""
31. 動詞
動詞の表層形をすべて抽出せよ．

32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""
def ExtractVerbs(lst):
    for m_dic in lst:
        if m_dic["pos"] == "動詞":
            m_dic["surf"]
            #print m_dic["surf"]           # chap4_1
            m_dic["base"]
            #print m_dic["base"]           # chap4_2

"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""
def ExtractNouns(lst):
    for m_dic in lst:
        if m_dic["pos"] == "名詞" and m_dic["pos1"] == "サ変接続":
            m_dic["surf"]
            #print m_dic["surf"] # chap4_3

"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""
def ExtractNounPhrase(lst):
    flag   = 0
    phrase = ""
    
    for m_dic in lst:
        if flag == 0 and m_dic["pos"] == "名詞":
            phrase += m_dic["surf"]
            flag = 1
        elif flag == 1 and m_dic["surf"] == "の":
            phrase += m_dic["surf"]
            flag = 2
        elif flag == 2 and m_dic["pos"] == "名詞":
            phrase += m_dic["surf"]
            print phrase
            flag = 0
            phrase = ""
        else:
            flag   = 0
            phrase = ""
            
        
def main():
    lst = MakeMorphoDic("./neko.txt.mecab") # chap4_0
    ExtractVerbs(lst)
    ExtractNouns(lst)
    ExtractNounPhrase(lst)
    
if __name__ == "__main__":
    main()
