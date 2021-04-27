# バインダーのポケットの数nと名刺の番号m
# n(バインダーのポケットの数) m(名刺の番号)
import pprint
n, m = [int(i) for i in input().split()]


# 裏の番号
back = 2 * n
# 裏の番号の保存
hoge = back

# バインダー
binder = {}
if n > m:
    number = 2 * n + 1
else:
    number = m + 1

for i in range(1, number):
    binder[i] = back
    back -= 1
    if hoge == i:
        back = hoge + (2 * n)
        hoge = back

print(binder[m])
