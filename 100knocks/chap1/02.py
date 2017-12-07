'''
・"coding:utf-8"とか書かなくてもOK
・text_connection()に直接パトカータクシーを代入した方がいいかも
・出力が以下だったので，"パタトクカシーー"以外はprintしないようにしよう
8
パタ
パタトク
パタトクカシ
パタトクカシーー
・zip()を使うと便利
・関数内でprint()表示するより，returnして，main関数でprintした方が関数っぽい
'''
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．


def text_connection(arr1, arr2):
    # zip関数を使うと，arr1とarr2の文字列の拡張for文的なものができる
    temp = ''
    for x, y in zip(arr1, arr2):
        temp += (x + y)

    return temp


if __name__ == '__main__':
    ans = text_connection('パトカー', 'タクシー')
    print(ans)

    # arr1が1文字多い場合
    ans = text_connection('パトカーパ', 'タクシー')
    print(ans)

    # arr2が1文字多い場合
    ans = text_connection('パトカー', 'タクシータ')
    print(ans)
