'''
・islower()使うといいよ
'''
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．
# 今回の例文は,I Lost My Wallet

import re  # 何度目の正規表現


def code_solution(str):
    str = list(str)
    words_list = []

    for x in str:
        # a-z残文字列を探す
        if re.search('[a-z]', x):
            words_list.append(chr(219 - ord(x)))
        else:
            words_list.append(x)

    return "".join(words_list)


if __name__ == '__main__':
    sentence = "I Lost My Wallet"

    print(code_solution(sentence))
    print(code_solution(code_solution(sentence)))


'''
以下，過去の自分が作ったコード
'''
# text = "Hello, World. My name is Tom! Nice to meet you."
#
# result = ""
# for t in text:
#     if t.islower():
#         result += chr(219 - ord(t))
#     else:
#         result += t
# print(result)
