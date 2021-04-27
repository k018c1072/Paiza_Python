# 町の大きさを表す 2 つの整数 H, W
# 町が縦 H マス、横 W マスのグリッドで表されることを意味しています。
H, W = [int(i) for i in input().split()]

# ねずみ小僧の初期位置を表す 2 つの整数 h0, w0
# ねずみ小僧が座標 (h0, w0) にある家から出発することを表しています。
h0, w0 = [int(i) - 1 for i in input().split()]

# 町にあるそれぞれの家が庶民の家か富豪の家かを表す文字列を入力
# "." であるとき、座標 (i, j) にある家が庶民の家
# "*" であるとき、座標 (i, j) にある家が富豪の家
town = [[0 for w in range(W + 1)] for h in range(H + 1)]
for h in range(H):
    str = list(input())
    cnt = 0
    for w in range(W):
        town[h][w] = str[cnt]
        cnt += 1

n = True  # 北
e = False  # 東
s = False  # 南
w = False  # 西
while True:
    try:
        if town[h0][w0] == ".":
            town[h0][w0] = "*"
            if n:
                n = False
                e = True
                w0 += 1
            elif e:
                e = False
                s = True
                h0 += 1
            elif s:
                s = False
                w = True
                w0 -= 1
            else:
                w = False
                n = True
                h0 -= 1
        elif town[h0][w0] == "*":
            town[h0][w0] = "."
            if n:
                n = False
                w = True
                w0 -= 1
            elif e:
                e = False
                n = True
                h0 -= 1
            elif s:
                s = False
                e = True
                w0 += 1
            else:
                w = False
                s = True
                h0 += 1
        else:
            break
    except:
        break

for h in range(H):
    for w in range(W):
        print(town[h][w], end="")
    print()
