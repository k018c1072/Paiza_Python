N = int(input())

flower = [[int(i) for i in input().split()] for j in range(N)]
x = list()
count = 0
max = 0
date = 10000

for i, j in flower:
    x.append(i + j)

for i in x:
    for j in x:
        if i == j:
            count += 1
            if max < count and date >= i:
                max = count
                date = i
    count = 0

print(date)
