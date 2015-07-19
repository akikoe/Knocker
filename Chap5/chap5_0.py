#!/usr/bin/env python
# coding: utf-8

"""
前準備:
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
"""

import re
import sys

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
    def __init__(self, tokens, chunk_lst):
        m_lst = []
        p = re.compile(u"<tok id=.*?</tok>")
        token_lst = p.findall(tokens)
        for j in token_lst:
            m_lst.append(Morph(j))
        self.morphs = m_lst # 形態素(Morphオブジェクト)のリスト
                 
        p = re.compile(u"<chunk id=\"(.*?)\" link=\"(.*?)\".*?</chunk>")
        m = p.match(tokens)
        self.dst  = int(m.group(2))  # 係り先の文節インデックス番号
        self.scrs = [i for i, c in enumerate(chunk_lst) if c.dst == int(m.group(1))] # 係り元文節インデックス番号のリスト
        
def make_chunk(path):
    lst = read(path)
    
    chunk_lst, c_lst = [], []
    p = re.compile(u"<chunk id=.*?</chunk>")
    for i in lst:
        tokens_lst = p.findall(i)
        for j in tokens_lst:
            c_lst.append(Chunk(j, c_lst))
        chunk_lst.append(c_lst)
        c_lst = []
    return chunk_lst


def show_chunk(lst): # 8文目の文節の文字列と係り先を表示
    for i in lst[7]:
        moji = ""
        for j in i.morphs:
            moji += j.surface
        print moji, i.dst

"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""
def add_words(lst, moji):
    for k in lst: # chunk中の単語
        if k.pos != "記号":
            moji+= k.surface
    return moji 

def show_dependency(lst):
    for i in lst:
        for j in i: # 1文中のchunk
            moji = ""
            moji = add_words(j.morphs, moji)
            moji += "\t"
            if j.dst > -1:
                moji = add_words(i[j.dst].morphs, moji)
            print moji

"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""
def show_nv_dependency(lst):
    for i in lst:
        for j in i: # 1文中のchunk
            moji = ""
            if "名詞" in [k.pos for k in j.morphs]:
                moji = add_words(j.morphs, moji)
                moji += "\t"
                if j.dst > -1:
                    morphs = i[j.dst].morphs
                    if "動詞" in [k.pos for k in morphs]:
                        moji = add_words(morphs, moji)
                        print moji

"""
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""
def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()
    
def convert_dotlang(lst, i):
    data ="digraph sample {\n" # はじまり
    for j in lst[i]: # 1文中のchunk
        moji, moji2 = "", ""
        moji = add_words(j.morphs, moji)
        if j.dst > -1:
            moji2 = add_words(lst[i][j.dst].morphs, moji2)
        else:
            break
        data += "%s -> %s;\n" % (moji, moji2)
    data += "}"
    
    write_file("./token.dot", data) # DOT言語作成
    """
    画像に変換
    $ dot -Tpng token.dot -o token.png
    """
    
"""
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
###
始める  で
見る    は を
###
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""
def extract_kaku_pattern(lst):
    for i in lst[7:8]:
        for j in i: # 1文中のchunk
            moji = ""
            for k in j.morphs:
                if k.pos == "動詞":
                    moji += k.base # 動詞の基本形
                    joshi_lst = []
                    for cnum in j.scrs:
                        morphs = i[cnum].morphs
                        joshi_lst += [k.surface for k in morphs
                                      if k.pos == "助詞"]
                    moji += "\t" + " ".join(joshi_lst)
                    print moji

"""
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを
"""
def extract_kaku_VPpattern(lst):
    for i in lst[7:8]: # 8文目
        for j in i: # 1文中のchunk
            moji = ""
            for k in j.morphs:
                if k.pos == "動詞":
                    moji += k.base # 動詞の基本形
                    joshi_lst, phrase_lst = [], []
                    for cnum in j.scrs:
                        morphs = i[cnum].morphs
                        joshi_lst  += [k.surface for k in morphs
                                                if k.pos == "助詞"]
                        phrase_lst += ["".join([k.surface for k in morphs])]
                    moji += "\t" + " ".join(joshi_lst) + "\t" + " ".join(phrase_lst)
                    print moji
    
def main():
    # Chap5_0
    morph_lst = make_morph("./neko.txt.cabocha")
    show_morph(morph_lst)

    # Chap5_1
    chunk_lst = make_chunk("./neko.txt.cabocha")
    show_chunk(chunk_lst)

    # Chap5_2
    show_dependency(chunk_lst)

    # Chap5_3
    show_nv_dependency(chunk_lst)

    # Chap5_4
    convert_dotlang(chunk_lst, 10)

    # Chap5_5
    extract_kaku_pattern(chunk_lst)

    # Chap5_6
    extract_kaku_VPpattern(chunk_lst)
    
if __name__ == "__main__":
    main()       
