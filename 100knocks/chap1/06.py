'''
・全体的に見にくい
・前に自分が作ったもの載せときます
・ここについての説明は今度直接話します
'''
# 06. 集合


def n_gram(input, n):
    temp = []
    for i in range(0, len(input)-n+1):
        temp.append(input[i: i+n])
    return temp


if __name__ == '__main__':
    s1 = "paraparaparadise"
    s2 = "paragraph"

    X, Y = set(n_gram(s1, 2)), set(n_gram(s2, 2))

    print("X =", X)
    print("Y =", Y)

    print("和 =", X.union(Y))
    print("積 =", X.intersection(Y))
    print("差 =", X.difference(Y))

    print("se in X =", "se" in X)
    print("se in Y =", "se" in Y)


