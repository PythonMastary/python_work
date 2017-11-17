'''
・引数名にstrはstr()とかぶるからあまりよろしくない　
　　str, list, intとかの変数/引数名はダメ
・最初に[]というから配列ができてしまってるのでNG
・問題文「連想配列（辞書型もしくはマップ型）を作成せよ．」
　　辞書型を作ろう！　リスト型で作っちゃだめ
'''
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might
# Also Sign Peace Security Clause. Arthur King Can. という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は
# 先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
# 連想配列（辞書型もしくはマップ型）を作成せよ．

import re


def atomic_dic(s):
    atomic_dict = {}
    single_number = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    # 文字列に分割(．は無視
    words = re.split('\s', s.replace('.', ''))

    # {番号: 単語}の辞書を作成
    for index, word in enumerate(words):
        # single_numberというリストの中に，indexがないかif文でチェック（解説）
        if index not in single_number:
            atomic_dict.update({index: word[:1]})
        else:
            atomic_dict.update({index: word[:2]})

    return atomic_dict


if __name__ == "__main__":
    w = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. ' \
               'New Nations Might Also Sign Peace Security Clause. Arthur ' \
               'King Can.'
    ans = atomic_dic(w)

    print(ans)
