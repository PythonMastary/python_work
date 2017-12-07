'''
・# コメント　の下に関数書くときは2行空行を挟もう

'''
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．


def template_sentence(str1, str2, str3):
    print(u"{0}時の{1}は{2}".format(str1, str2, str3))


if __name__ == '__main__':
    template_sentence(12, "気温", 22.4)
