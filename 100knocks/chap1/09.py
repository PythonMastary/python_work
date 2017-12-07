# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文
# （例えば"I couldn't believe that I could actually understand what I was reading
# : the phenomenal power of the human mind ."）
# を与え，その実行結果を確認せよ．○
import re
import random


def typoglycemia(sentence):
    # 文字列に分割(．は無視
    words = re.split('\s', sentence.replace('.', ''))

    # 分割した文字を格納するリスト
    words_list = []

    for i in range(0, len(words)):
        if len(words[i]) < 4:
            words_list.insert(i, words[i])
        else:
            ran_str_list = list(words[i][1:-1])
            random.shuffle(ran_str_list)

            # 先頭と末尾以外を並び替え
            words_list.append(
                words[i][0] + "".join(ran_str_list) + words[i][-1]
            )

    return words_list


if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what " \
               "I was reading : the phenomenal power of the human mind ."
    ans = typoglycemia(sentence)

    print(ans)
