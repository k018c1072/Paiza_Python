N = int(input())
botan = [int(input()) for i in range(N)]

now = 0
count = 0
while True:
    now = botan[now] - 1
    count += 1
    if count == N:
        print('-1')
        break
    if now == 1:
        print(count)
        break
