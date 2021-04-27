# 表の行数を表す整数 H と 列数を表す整数 W
H, W = [int(i) for i in input().split()]

# 1 行目にある整数の 2 要素 a_1, a_2
a_1, a_2 = [int(i) for i in input().split()]
# 2 行目にある整数の 2 要素 b_1, b_2
b_1, b_2 = [int(i) for i in input().split()]

table = [[0 for i in range(W)] for j in range(H)]
table[0][0] = a_1
table[0][1] = a_2
table[1][0] = b_1
table[1][1] = b_2

for h in range(H):
    for w in range(W):
        if w >= 2:
            table[h][w] = table[h][w - 1] - table[h][w - 2] + table[h][w - 1]
        elif h >= 2:
            table[h][w] = table[h - 1][w] - table[h - 2][w] + table[h - 1][w]
for h in range(H):
    for w in range(W):
        print(str(table[h][w]), end="")
        if w < W - 1:
            print(" ", end="")
    print()
