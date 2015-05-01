#!/usr/bin/env python
# coding: utf-8

"""
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""

def reverse(lst):
    n = len(lst)
    for i in range(n/2):
        j      = n-i-1
        jtem   = lst[j] # 最後の要素
        lst[j] = lst[i]
        lst[i] = jtem
    return lst

def main():
    mojis    = "stressed"
    print "before:", mojis
    
    moji_lst = list(mojis)     # string -> list 
    re_lst   = reverse(moji_lst)
    re_mojis = "".join(re_lst) # list -> string

    print "after: ", re_mojis # moji_lst[::-1]

if __name__ == "__main__":
    main()
