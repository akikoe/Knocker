#!/usr/bin/env python
# coding: utf-8

"""
第6章: 英語テキストの処理

前準備
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
"""
import xml.etree.ElementTree as ET

"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
$ java -cp stanford-corenlp-3.5.2.jar:stanford-corenlp-3.5.2-models.jar:xom.jar:joda-time.jar:jollyday.jar:ejml-3.5.2.jar -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -file ~/GitHub/Knocker/Chap6/nlp.txt
-> nlp.txt.xmlファイルが生成される　
"""

def read_xml(path):
    tree = ET.parse(path)
    return tree

def tokenize_xml(tree):
    wrd_lst = []
    root = tree.getroot()
    for token in root.findall('.//token'):
        wrd_lst.append(token.find('word').text)
    return wrd_lst

def main():
    tree = read_xml("./nlp.txt.xml")
    wrd_lst = tokenize_xml(tree)
    print ("\n".join(wrd_lst))

if __name__ == '__main__':
    main()
