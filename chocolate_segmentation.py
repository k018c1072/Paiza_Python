# チョコの列数と行数を表す整数
H, W = map(int, input().split())

# チョコ初期化
chocolates = [0] * H

# H 行 には W 個の整数が半角スペース区切りで与えられます。
for h in range(H):
    c = list(map(int, input().split()))
    chocolates[h] = c

count = 0
check = []
for h in range(H):
    total = sum(chocolates[h])
    left = 0
    for w in range(W):
        left += chocolates[h][w]
        right = total - left
        if left == right:
            check.append(w)
            count += 1
            break

if count == H:
    print("Yes")
    for h in range(H):
        print("A" * (check[h] + 1) + "B" * (W - (check[h] + 1)))
else:
    print("No")
