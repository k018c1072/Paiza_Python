# M は立候補者の人数を、N は有権者の人数を、K は演説が行われる回数
M, N, K = [int(i) for i in input().split()]

# 演説の順番
Order = []
for k in range(K):
    Order.append(int(input()))

# 支持者数辞書初期化
Supporter = {}
for m in range(M):
    Supporter[m + 1] = 0

for o in Order:
    for key, value in Supporter.items():
        if o != key and value > 0:
            Supporter[o] += 1
            Supporter[key] -= 1
    if N > 0:
        Supporter[o] += 1
        N -= 1

max_value = 0
max_key = []
for key, value in Supporter.items():
    if max_value < value:
        max_value = value
        max_key.clear()
        max_key.append(key)
    elif max_value == value:
        max_key.append(key)

for k in max_key:
    print(k)
