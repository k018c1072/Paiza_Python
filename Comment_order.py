# コメントの数を表す整数 N
import pprint
N = int(input())

# コメント
com = []
for n in range(N):
    c, r, g = [str(i) for i in input().split()]
    com.append({'Cid': c, 'Rid': r, 'Good': int(g)})

# Goodの合計


def goodsum(r, g, i):
    for n in range(N):
        if com[n]['Cid'] == r:
            com[n]['Good'] += g
            com[i]['Good'] = 0
            if com[n]['Rid'] != 'None':
                goodsum(com[n]['Rid'], com[n]['Good'], n)
            else:
                return True


for n in range(N):
    if com[n]['Rid'] != 'None':
        goodsum(com[n]['Rid'], com[n]['Good'], n)

gmax = 0
cid = 0
for n in range(N):
    if com[n]['Rid'] == 'None':
        if com[n]['Good'] > gmax:
            gmax = com[n]['Good']
            cid = com[n]['Cid']
        elif com[n]['Good'] == gmax:
            if int(com[n]['Cid']) < int(cid):
                gmax = com[n]['Good']
                cid = com[n]['Cid']
print(cid)
