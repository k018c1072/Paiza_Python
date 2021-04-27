# 回転する回数を表す整数 N、マス目の縦の大きさを表す整数 H、マス目の横の大きさを表す整数 W
import pprint
N, H, W = [int(i) for i in input().split()]

# 最初にサイコロを置く行を表す整数 sy と最初にサイコロを置く列を表す整数 sx
sy, sx = [int(i) - 1 for i in input().split()]
# 移動方法を表す N 文字の文字列 direction(方向)
dir = list(input())

# サイコロ初期化
dict = {'front': '5', 'rear': '2', 'top': '1',
        'under': '6', 'left': '3', 'right': '4'}

# マス
trout = [['0' for i in range(W)] for j in range(H)]
trout[sy][sx] = dict['under']


def roll(d):
    if d == 'U' or d == 'D':
        if d == 'U':
            hoge = dict['front']
            dict['front'] = dict['under']
            dict['under'] = dict['rear']
            dict['rear'] = dict['top']
            dict['top'] = hoge
            return dict['under']
        else:
            hoge = dict['front']
            dict['front'] = dict['top']
            dict['top'] = dict['rear']
            dict['rear'] = dict['under']
            dict['under'] = hoge
            return dict['under']
    else:
        if d == 'L':
            hoge = dict['left']
            dict['left'] = dict['top']
            dict['top'] = dict['right']
            dict['right'] = dict['under']
            dict['under'] = hoge
            return dict['under']
        else:
            hoge = dict['right']
            dict['right'] = dict['top']
            dict['top'] = dict['left']
            dict['left'] = dict['under']
            dict['under'] = hoge
            return dict['under']


count = 0
while count < N:
    if dir[count] == 'U':
        sy -= 1
    elif dir[count] == 'D':
        sy += 1
    elif dir[count] == 'L':
        sx -= 1
    else:
        sx += 1
    trout[sy][sx] = roll(dir[count])
    count += 1

for h in range(H):
    for w in range(W):
        print(trout[h][w], end="")
        if w + 1 < W:
            print(end=" ")
    print()
