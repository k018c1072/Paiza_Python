n = int(input())
m = int(input())

r = []
for i in range(m):
    r.append(input())

r2 = r

for i in r:
    for j in list(i):
        if n == int(j):
            r2.remove(i)
            print(r2)
            break

print(r2)
