import math

N, M = [int(i) for i in input().split()]
Point = 0
for i in range(M):
    Fare = int(input())
    if Point >= Fare:
        Point -= Fare
    else:
        N -= Fare
        Point += Fare * 0.1
    print(str(N) + " " + str(math.floor(Point)))
