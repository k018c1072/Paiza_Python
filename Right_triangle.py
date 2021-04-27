M, N = [int(i) for i in input().split()]

if (M > N):
    Hypotenuse = M
else:
    Hypotenuse = N
count = 0
ansarray = []

for i in range(1, M):
    for j in range(1, N):
        c = i * i + j * j
        for x in range(1, Hypotenuse + 1):
            y = x * x
            if c == y:
                ansarray.append(x)
                count += 1

print(ansarray)
print(count)
