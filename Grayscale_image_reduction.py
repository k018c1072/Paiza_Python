# 1 行目には入力される画像のサイズを表す整数 N および縮小の倍率を表す整数 Kが入力される。
N, K = [int(i) for i in input().split()]

# 続く N 行には各ピクセルの画素値が入力されます。
# すなわち、a_ij は画像の i 行目、j 列目のピクセルの画素値を表す整数です。
image = [[int(i) for i in input().split()] for j in range(N)]

# K × K ピクセルのブロックを初期化
new_image = [[0 for i in range(int(N / K))] for j in range(int(N / K))]

for i in range(N):
    for j in range(N):
        new_image[int(i / K)][int(j / K)] += image[i][j]

for i in range(int(N / K)):
    for j in range(int(N / K)):
        new_image[i][j] = int(new_image[i][j] / (K * K))
        print(new_image[i][j], end="")
        if j + 1 != int(N / K):
            print(" ", end="")
    print()
