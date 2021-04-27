# 1 行目にチェスボードの大きさを表す整数 N、
# 駒を置く位置を表す整数 H、W、
# 駒を動かせる回数を表す整数 K がこの順で半角スペース区切りで与えられます。
N, H, W, K = [int(i) for i in input().split()]

# 縦 N マス、横 N マスのチェスボード
Chess_board = [[0 for i in range(N)] for j in range(N)]
Chess_board[H][W] = 1


def Upper_right(h, w):
    try:
        if Chess_board[h - 1][w + 1] == 0:
            return True
    except:
        return False


def Right_below(h, w):
    try:
        if Chess_board[h + 1][w + 1] == 0:
            return True
    except:
        return False


def Upper_left(h, w):
    try:
        if Chess_board[h - 1][w - 1] == 0:
            return True
    except:
        return False


def Left_below(h, w):
    try:
        if Chess_board[h + 1][w - 1] == 0:
            return True
    except:
        return False
