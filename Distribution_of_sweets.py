M, N = [int(i) for i in input().split()]

container = []
for i in range(M):
    container.append(int(input()))

remaining = []  # 容器の数
sweets = []  # お菓子の余り数（少なく方が良い）
counter = 1  # お菓子カウンター

for i in range(M):
    for remcounter in range(2, container[i]):
        while N - (remcounter * counter) > 0 and remcounter <= container[i]:
            sweets.insert(i, N - (remcounter * counter))
            remaining.insert(i, counter)
            counter += 1
        counter = 1

Aremaining = remaining[0]
Asweets = sweets[0]
ans = 0

for i in range(M):
    if Asweets > sweets[i]:
        ans = i
    elif Asweets >= sweets[i] and Aremaining < remaining[i]:
        ans = i

print(ans)
