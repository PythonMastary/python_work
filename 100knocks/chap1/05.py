'''
・おそらく，ngramのライブラリをpipとかで入れたと思うけど，レビューする人がその
　　ライブラリを持っていないことを配慮しよう
　もし．必ずこのライブラリが必要ならば，このコードではなくて，readme.txtなどを作成して
　　「pip install ngram する必要があります」などの注釈を書かないとダメ
　ライブラリを書かなくてもできるのなら，できるだけ使わない方がいい
・単語bi-gramの出力が見辛いかも
'''
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ

import re


def tango_n_gram(s, n):
    temp = []
    word_list = re.sub("[,.]", "", s).split()

    for i in range(0, len(word_list)-n+1):
        temp.append(word_list[i: i+n])
    return temp


def mozi_n_gram(s, n):
    temp = []
    if len(s) >= n:
        for i in range(len(s)+1-n):
            temp.append(s[i:i+n])

    return temp


if __name__ == '__main__':
    s = "I am an NLPer"

    ans = tango_n_gram(s, 2)
    print("単語:", ans)

    ans = mozi_n_gram(s, 2)
    print("文字列:", ans)
