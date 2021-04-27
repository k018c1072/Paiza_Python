# 非負の整数a, b(a ≤ b)と 、 正の整数xが与えられます 。
# a以上b以下の整数のうち 、 xで割り切れるものの個数を求めてください 。
a, b, x = [int(i) for i in input().split()]

cou = 0
for i in range(a, b + 1):
    if i % x == 0:
        cou += 1

print(cou)
