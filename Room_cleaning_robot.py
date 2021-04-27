import pprint
Right = False
Left = False
Under = False
Up = False
c = False
count = 0
h = 0
w = 0


# 掃除ロボットが掃除する時間を表す整数 N
N = int(input())

# 部屋の縦と横のマスの数を表す整数 H, W
H, W = [int(i) for i in input().split()]

# 部屋を初期化
# "#" は汚れたマスを、"." は汚れてないマス
room = [[i for i in list(input())] for j in range(H)]


def clean(c):
    if c == "#":
        return 1
    else:
        return 0

# 方向


def direction():
    global w
    global h
    if Right:
        w += 1
    elif Left:
        w -= 1
    elif Up:
        h -= 1
    elif Under:
        h += 1


# 四隅の保存
ul_y = 0
ul_w = 0
ur_y = 0
ur_w = W - 1
ll_y = H - 1
ll_w = 0
lr_y = H - 1
lr_w = W - 1

"""
# 四隅か判定
def check():
    global h
    global w
    global ul_y
    global ul_w
    global ur_y
    global ur_w
    global ll_y
    global ll_w
    global lr_y
    global lr_w
    if h == ul_y and w == ul_w:
        Up = False
        Right = True
        ul_y += 1
        ul_w += 1
    elif h == ur_y and w == ur_w:
        Right = False
        Under = True
        ur_y += 1
        ur_w -= 1
    elif h == lr_y and w == lr_w:
        Under = False
        Left = True
        lr_y -= 1
        lr_w -= 1
    elif h == ll_y and w == ll_w:
        Left = False
        Up = True
        ll_y -= 1
        ll_w += 1
"""

for n in range(N):
    count += clean(room[h][w])
    room[h][w] = '★'
    if h == ul_y and w == ul_w:
        Up = False
        Right = True
        ul_y += 1
        if c:
            ul_w += 1
        c = True
    elif h == ur_y and w == ur_w:
        Right = False
        Under = True
        ur_y += 1
        ur_w -= 1
    elif h == lr_y and w == lr_w:
        Under = False
        Left = True
        lr_y -= 1
        lr_w -= 1
    elif h == ll_y and w == ll_w:
        Left = False
        Up = True
        ll_y -= 1
        ll_w += 1
    direction()

print(count)
