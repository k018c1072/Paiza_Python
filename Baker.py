# パンの種類数を表す整数 N とクエリの個数を表す整数 Q
import pprint
N, Q = [int(i) for i in input().split()]

# パン
Bread = {}

# N 行のうちの i 行目 (1 ≦ i ≦ N) には、i 番目のパンの値段を表す整数 a_i と
# 今日の初めの時点での i 番目のパンの在庫数を表す整数 b_i
for i in range(1, N + 1):
    p, s = [int(j) for j in input().split()]
    Bread[i] = {'price': p, 'stock': s}

# 処理
processing = []

# bake処理


def bake(p):
    for i in range(1, N + 1):
        Bread[i]['stock'] += int(p[i])

# buy処理


def buy(p):
    # 最初に足りないパンがあるかチェック
    for i in range(1, N + 1):
        if Bread[i]['stock'] < int(p[i]):
            return - 1

    # 在庫処理と購入に必要な金額を計算
    total = 0
    for i in range(1, N + 1):
        total += Bread[i]['price'] * int(p[i])
        Bread[i]['stock'] -= int(p[i])
    return total


# Q 行のうちの i 行目 (1 ≦ i ≦ Q) には、i 番目のクエリのタイプを表す文字列 q_i と、
# それぞれのクエリで扱われる 1 種類目のパンの個数を表す整数 c_{i, 1},
# 2 種類目のパンの個数を表す整数 c_{i, 2}, ..., N 種類目のパンの個数を表す整数 c_{i, N}
for q in range(Q):
    processing = [i for i in input().split()]
    if processing[0] == 'bake':
        bake(processing)
    else:
        print(buy(processing))
