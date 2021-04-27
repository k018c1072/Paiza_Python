N, M, X = [int(i) for i in input().split()]

books = {}
for i in range(N):
    hoge = list(map(int, input().split()))
    books[i] = hoge

Achievement = False  # 達成

for n in range(2 ** N):
    conditions = [0 for m in range(M + 1)]  # 条件
    for i in range(N):
        if ((n >> i) & 1):
            for m in range(M + 1):
                conditions[m] += books[i][m]

    # 条件が達成しているか判定
    count = 0
    for m in range(1, M + 1):
        if conditions[m] < X:
            break
        count += 1
    if count == M:
        if Achievement == False:
            Achievement = True
            min = conditions[0]
        elif min > conditions[0]:
            min = conditions[0]

if Achievement == False:
    print(-1)
else:
    print(min)
