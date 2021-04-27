from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

N, M, K = [int(i) for i in input().split()]

# 辞書でアイテム種別ごとの得点を決定
items_point = {}
point = [float(i) for i in input().split()]
for i in range(N):
    items_point[i] = point[i]

# ユーザごとのアイテムの数を入力
users_items = [[0 for i in range(N)] for i in range(M)]  # 初期化
for i in range(M):
    n = 0
    for j in input().split():
        users_items[i][n] = int(j)
        n += 1

# ユーザごとの総合点を決定
users_point = []
for i in range(M):
    total = 0
    for j in range(N):
        total += users_items[i][j] * items_point[j]
    users_point.append(Decimal(total).quantize(
        Decimal('0'), rounding=ROUND_HALF_UP))
users_point.sort()

# 後ろから表示
j = -1
for i in range(K):
    print(users_point[j])
    j += -1
