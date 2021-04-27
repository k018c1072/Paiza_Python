# スゴロクのマスの数を表す整数 : N
# プレイヤーの人数を表す : M
# 各プレイヤーがサイコロを振る回数を表す整数 : K
N, M, K = list(map(int, input().split()))

effect = {}
for n in range(1, N - 1):
    b, c = input().split()
    effect[n] = {"move": int(b), "coin": int(c)}

#protruding_eyes : 出目
pe = []
player = {}
for i in range(K):
    pe.append(list(map(int, input().split())))
    for j in range(M):
        player[j] = {'mass': 0, "coin": 0, 'rank': 0}


def bonus(j, num):
    if player[j]['rank'] == 1:
        player[j]['coin'] += num * 3
    elif player[j]['rank'] == 2:
        player[j]['coin'] += num * 2
    else:
        player[j]['coin'] += num


rank = 1
for i in range(K):
    for j in range(M):
        if 0 < player[j]['rank'] < 4:
            bonus(j, pe[i][j])
            continue
        player[j]['mass'] += pe[i][j]
        if player[j]['mass'] < N:
            player[j]['coin'] += effect[player[j]['mass']]['coin']
            player[j]['mass'] += effect[player[j]['mass']]['move']
        if player[j]['mass'] >= N - 1:
            player[j]['rank'] = rank
            rank += 1
        if player[j]['mass'] < 0:
            player[j]['mass'] = 0
        if player[j]['coin'] < 0:
            player[j]['coin'] = 0

first = 0
max = 0
for j in range(M):
    if max < player[j]['coin']:
        max = player[j]['coin']
        first = j

print(first + 1, max)
