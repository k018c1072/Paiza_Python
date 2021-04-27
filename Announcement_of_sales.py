N, R = map(int, input().split())

Earnings = []  # 売上
for i in range(N):
    Earnings.append(int(input()) / R)

# 売上最大値
Maximum_sales = max(Earnings)

cnt = 1
for ear in Earnings:
    print(str(cnt) + ":", end="")
    for i in range(int(ear)):
        print("*", end="")
    for i in range(int(Maximum_sales - ear)):
        print('.', end='')
    print()
    cnt += 1
