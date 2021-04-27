# 開始地点の x 座標、y 座標を表す整数 s_x, s_y
s_x, s_y = [int(i) for i in input().split()]

# 実験対象のロボットの前方向、右方向、後方向、左方向への
#  1 歩の移動コマ数を表す整数 d_f, d_r, d_b, d_l
d_f, d_r, d_b, d_l = [int(i) for i in input().split()]

# 命令の個数を表す整数 N
N = int(input())

# 方向
direction = 'N'


# 移動


def move(c_i):
    global s_x, s_y, direction
    if direction == 'N':
        if c_i == 'F':
            s_y += d_f
        elif c_i == 'R':
            s_x += d_r
        elif c_i == 'L':
            s_x -= d_l
        elif c_i == 'B':
            s_y -= d_b
    elif direction == 'E':
        if c_i == 'F':
            s_x += d_f
        elif c_i == 'R':
            s_y -= d_r
        elif c_i == 'L':
            s_y += d_l
        elif c_i == 'B':
            s_x -= d_b
    elif direction == 'S':
        if c_i == 'F':
            s_y -= d_f
        elif c_i == 'R':
            s_x -= d_r
        elif c_i == 'L':
            s_x += d_l
        elif c_i == 'B':
            s_y += d_b
    elif direction == 'W':
        if c_i == 'F':
            s_x -= d_f
        elif c_i == 'R':
            s_y += d_r
        elif c_i == 'L':
            s_y -= d_l
        elif c_i == 'B':
            s_x += d_b


# 方向転換
def turning(c_i):
    global direction
    if c_i == 'R':
        if direction == 'N':
            direction = 'E'
        elif direction == "E":
            direction = 'S'
        elif direction == 'S':
            direction = 'W'
        elif direction == 'W':
            direction = 'N'
    elif c_i == 'L':
        if direction == 'N':
            direction = 'W'
        elif direction == "W":
            direction = 'S'
        elif direction == 'S':
            direction = 'E'
        elif direction == 'E':
            direction = 'N'
    elif c_i == 'B':
        if direction == 'N':
            direction = 'S'
        elif direction == "W":
            direction = 'E'
        elif direction == 'S':
            direction = 'N'
        elif direction == 'E':
            direction = 'W'

# N 行のうち i 行目 (1 ≦ i ≦ N) について命令の種類、
# 内容を表す文字 e_i, c_i がこの順に半角スペース区切りで与えられます。
# 命令の種類が「移動」のとき e_i は "m"、「方向転換」の場合は "t"
# 命令が「移動」のとき c_i は移動方向を表し、命令が「方向転換」のとき c_i は転換する方向を表します。
# 前方向、右方向、後方向、左方向の順に "F", "R", "B", "L" で表されます。


for n in range(N):
    e_i, c_i = [i for i in input().split()]
    if e_i == 'm':
        move(c_i)
    else:
        turning(c_i)
print(str(s_x) + " " + str(s_y))
