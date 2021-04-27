import math

M = int(input()) + 0.0
N = int(input())

Fax = [[int(i) for i in input().split()]for j in range(N)]
hours = Fax[0][0]
paper = 0
total = 0

for i, j, k in Fax:
    if hours == i:
        paper += k
    else:
        total += math.ceil(paper / M)
        paper = 0
        hours = i
        paper += k
total += math.ceil(paper / M)
print(total)
