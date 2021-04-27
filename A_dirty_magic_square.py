# 魔方陣の大きさ N
N = int(input())

# 続く N 行のうちの n 行目 (1 ≦ n ≦ N) には N 個の整数が半角スペース区切りで与えられます。
# n 行目の i 番目 (1 ≦ n ≦ N) の整数 m_{n, i} は作った魔方陣の n 行 i 列目の数を表します。
# ただし、コーヒーをこぼして見えなくなった部分は 0 になっています。
Magic_square = [[int(i) for i in input().split()]for n in range(N)]

# 1 から N^2 までの数字
numbers = []
for n in range(1, N * N + 1):
    numbers.append(n)

# 消えている数字を特定する
Dirty_place = []
for n in range(N):
    for i in range(N):
        if Magic_square[n][i] in numbers:
            numbers.remove(Magic_square[n][i])
        else:
            Dirty_place.append(n)
            Dirty_place.append(i)

# 数字を入れて総和を判定する
Magic_square[Dirty_place[0]][Dirty_place[1]] = numbers[0]
Magic_square[Dirty_place[2]][Dirty_place[3]] = numbers[1]


side = 0
for n in range(N):
    ans = 0
    for i in range(N):
        ans += Magic_square[n][i]
    if side == 0:
        side = ans
    elif side == ans:
        check_s = True
    else:
        check_s = False
        break

length = 0
for n in range(N):
    ans = 0
    for i in range(N):
        ans += Magic_square[i][n]
    if length == 0:
        length = ans
    elif length == ans:
        check_l = True
    else:
        check_l = False
        break

if check_s != True or check_l != True:
    Magic_square[Dirty_place[0]][Dirty_place[1]] = numbers[1]
    Magic_square[Dirty_place[2]][Dirty_place[3]] = numbers[0]

for n in range(N):
    for i in range(N):
        print(Magic_square[n][i], end="")
        if i != N - 1:
            print(" ", end="")
    print()
