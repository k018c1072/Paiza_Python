N = int(input())

candies = [[int(i) for i in input().split()] for j in range(2)]

max = 0
total = 0
for c in range(N):
    for n in range(N - c):
        total += candies[0][n]
    for n in range(N - c - 1, N):
        total += candies[1][n]
    if max <= total:
        max = total
    total = 0

print(max)
