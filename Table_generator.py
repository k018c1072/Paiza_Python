# 見出しの個数を表す整数 W
W = int(input())

# j 列目 (1 ≦ j ≦ W) の見出しを表す c_j が、c_1, c_2, ... c_W の順に半角スペース区切りで与える
heading = [h for h in input().split()]

# データ行の行数を表す整数 H
H = int(input())

# H 行のうちの i 行目 (1 ≦ i ≦ H) に、i 行 j 列目 (1 ≦ j ≦ W) のデータを表す
# 文字列 r_{i, j} が r_{i,1}, r_{i,2},...,r_{i,W} の順に半角スペース区切りで与えられます。
data = [[w for w in input().split()] for h in range(H)]

# 列ごとの最大の文字数を求める
max_length = [len(h) for h in heading]
for w in range(W):
    for h in range(H):
        if max_length[w] < len(data[h][w]):
            max_length[w] = len(data[h][w])


def blank(max_l, w):
    length = max_l - w
    while length != 0:
        print(" ", end="")
        length -= 1


# 見出し行を出力
for w in range(W):
    if w != 0:
        print(" | " + heading[w], end="")
    else:
        print("| " + heading[w], end="")
    blank(max_length[w], len(heading[w]))
print(" |")

# 見出し行とデータの間の行を出力
for w in range(W):
    print("|", end="")
    count = -2
    while max_length[w] > count:
        print("-", end="")
        count += 1
print("|")

# データ行を出力
for h in range(H):
    for w in range(W):
        if w != 0:
            print(" | " + data[h][w], end="")
        else:
            print("| " + data[h][w], end="")
        blank(max_length[w], len(data[h][w]))
    print(" |")
