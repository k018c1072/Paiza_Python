N, V = [int(i) for i in input().split()]
times = 0
position = 0
Judgment = "NO"
for i in range(N):
    T, P = [int(j) for j in input().split()]
    times = T - times
    position = P - position
    if (times != 0 and position != 0):
        if (position / times >= V):
            Judgment = "YES"
    times = T
    position = P
print(Judgment)
