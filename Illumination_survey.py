import math

# 並木道に並ぶ木の本数を表す整数 N および区間の電球の平均個数が上回らなければならない数を表す整数 M
N, M = [int(i) for i in input().split()]

# それぞれの木の電球
light_bulb = {}
tree = 1
for n in input().split():
    light_bulb[tree] = int(n)
    tree += 1

# 電球の数を調べたい区間の数を表す整数 Q
Q = int(input())

# 電球の数を調べたい区間の始点を表す整数 S_i、終点を表す整数 E_i (1 ≦ i ≦ Q)
for q in range(Q):
    light_ans = 0
    tree_count = 0
    s, e = [int(i) for i in input().split()]
    for key in range(s, e + 1):
        light_ans += light_bulb[key]
        tree_count += 1
    shortage = M - math.floor(light_ans / tree_count)
    if shortage < 0:
        shortage = 0
    for key in range(s, e + 1):
        light_bulb[key] += shortage

for key, value in light_bulb.items():
    print(str(value), end="")
    if key != N:
        print(" ", end="")
