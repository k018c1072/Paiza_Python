# ピースの個数を表す整数 X、パズルの大きさを表す整数 N、ピースの大きさを表す整数 M
import pprint
X, N, M = [int(i) for i in input().split()]

# h 行目 (1 ≦ h ≦ N) には "Y" および "B" からなる長さ N の文字列 C_h が与えられます。
# C_h の w 番目 (1 ≦ w ≦ N) の文字は完成形における h 行 w 列のマスの色を表し、
# "Y" は黄色を、"B" は青色を表します。
puzzle = []
puzzle = [[i for i in list(input())] for j in range(N)]
pprint.pprint(puzzle)

# h 行目の (1 ≦ h ≦ M) には "Y" および "B" からなる長さ N の文字列 P_{1, h} が与えられます。
# P_{1, h} の w 番目の文字は 1 個目のピースにおける h 行 w 番目のマスの色を表し、
# "Y" は黄色を、"B" は青色を表します。
# 以降 M × (X - 1) 行には 2 個目のピースから X 個目までのピースの情報が与えられます。

count = 0
while M * (X - 1) > count:
    piece = []
    piece = [[i for i in input()] for j in range(M)]

    count += 1
