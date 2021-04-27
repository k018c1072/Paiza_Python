# 福袋に詰める商品の価値の合計の最小値を表す整数 S
S = int(input())

# 福袋に詰める候補となる商品の数を表す整数 N
N = int(input())

# N 行のうちの i 行目 (1 ≦ i ≦ N) には、i 番目の商品の価値を表す整数 v_i
product = [[int(i) for i in input()] for j in range(N)]

for i in product:
    for j in range(i, product[-1]):
