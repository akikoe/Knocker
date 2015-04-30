#!/usr/bin/env python
# coding: utf-8

"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

 # Alternately concatenate 2 lists
def alt_concatenate(lst, lst2):
    words = ""
    for i, j in zip(lst, lst2): # Set the shorter length of lists to the range
        words += i + j
    return words
    

def main():
    mojis  = "パトカー"
    mojis2 = "タクシー"

    print "before:", mojis, mojis2
    u_mojis  = unicode(mojis,  "utf-8")  # -> unicode
    u_mojis2 = unicode(mojis2, "utf-8")
    mlst  = list(u_mojis)                # string -> list
    mlst2 = list(u_mojis2)
    words = alt_concatenate(mlst, mlst2) # lists -> string
    print "after: ", words

if __name__ == "__main__":
    main()
