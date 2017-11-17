'''
・importはファイルの頭に書こう（import文の上に2行以上の空行はダメ）
・"Now I need..."は，長すぎるので80文字手前で改行する
・関数とmain文の中に同じ変数名（sentence）を使うのはあまりよくない
　　main文の方はテキトーな変数でOK
　　関数名の方はちゃんとした表記にしよう
・each_words_counte  スペルミスの関数　ダメ
・詰め詰めのコードは見づらいので，適度に改行を挟む
・listという変数名はやめよう
　　list()というキャスト型とかぶるから
・for word in words:　のように，list型をfor文で回すことが可能
　　重要なテクニックなので覚えよう

'''
# "Now I need a drink, alcoholic of course, after the heavy lectures involving
# quantum mechanics."という文を単語に分解し各単語の（アルファベットの）文字数を先頭から
# 出現順に並べたリストを作成せよ．

import re


def each_words_count(sentence):
    '''文字列を分割し、各文字の文字数を調べる（ArgsとかReturnsを書かなくてもOK）'''

    temp = []

    # 文字列に分割(．は無視
    words = re.split('\s', sentence.replace('.', ''))

    for word in words:
        temp.append(len(word))

    return temp


if __name__ == "__main__":
    w = 'Now I need a drink, alcoholic of course, after the heavy lectures ' \
        'involving quantum mechanics.'
    ans = each_words_count(w)
    print(ans)
