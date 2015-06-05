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
from matplotlib import pyplot as plt

"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""
def MakeMorphoDic(path):
    lst, m_dic_lst   = [], []
    
    f = open(path, "r")
    line = f.readline()
    p = re.compile(u"(.*?)\t(.*)")
    while line:
        m_dic = {}
        line = line.rstrip()
        if line == "EOS":
            lst.append(m_dic_lst)
            m_dic_lst = []
        else:
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
    return lst

"""
31. 動詞
動詞の表層形をすべて抽出せよ．

32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""
def ExtractVerbs(lst):
    for sen in lst:
        for m_dic in sen:
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
    for sen in lst:
        for m_dic in sen:
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

    for sen in lst:
        #for dic1, dic2, dic2 in zip(m_dic[:], m_dic[1:], m_dic[2:]): # とすると短くかける
        for m_dic in sen:
            if flag == 0 and m_dic["pos"] == "名詞":
                phrase += m_dic["surf"]
                flag = 1
            elif flag == 1 and m_dic["surf"] == "の":
                phrase += m_dic["surf"]
                flag = 2
            elif flag == 2 and m_dic["pos"] == "名詞":
                phrase += m_dic["surf"]
                #print phrase
                flag = 0
                phrase = ""
            else:
                flag   = 0
                phrase = ""
            
"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""
def ExtractLongestNouns(lst):
    for sen in lst:
        phrase = []
        for m_dic in sen:
            if m_dic["pos"] == "名詞":
                phrase.append(m_dic["surf"])
            else:
                #if len(phrase) > 1: print ''.join(phrase)
                phrase = []

"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""
def SortWordFreq(lst):
    wdic = {}
    wlst  = []
    for sen in lst:
        for m_dic in sen:
            word = m_dic["surf"]
            if word in wdic:
                wdic[word] += 1
            else:
                wdic[word] = 1
    wlst = [(k, v) for k, v in wdic.items()]
    wlst = sorted(wlst, reverse=True, key=lambda x:x[1])
    #    for i in range(10):
    #        print wlst[i][0], wlst[i][1]
    return wlst

"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""
def DisplayTop10(wlst):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(u"単語の出現頻度")
    ax.set_xlabel(u"単語")
    ax.set_ylabel(u"出現頻度")
    ax.bar(range(10), [j for i, j in wlst[:10]], align="center")
    plt.xticks(range(10), [unicode(i, "utf-8") for i, j in wlst[:10]])
    plt.show()

"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""
def DisplayWordKind(wlst):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1) # プロット領域（1x1分割の1番目に領域を配置せよという意味）
    ax.set_title(u"出現頻度毎の単語の種類数")
    ax.set_xlabel(u"出現頻度")
    ax.set_ylabel(u"単語種類数")
    ax.hist([j for i, j in wlst])
    plt.show()

    
def main():
    lst = MakeMorphoDic("./neko.txt.mecab") # chap4_0
    ExtractVerbs(lst)
    ExtractNouns(lst)
    ExtractNounPhrase(lst)
    ExtractLongestNouns(lst)
    wlst = SortWordFreq(lst)
    #DisplayTop10(wlst)
    DisplayWordKind(wlst)
    
if __name__ == "__main__":
    main()
