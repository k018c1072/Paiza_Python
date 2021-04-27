# 表示する商品の数を表す整数 N、商品の指標の数を表す整数 M
N, M = [int(i) for i in input().split()]

# i 番目の商品の j 番目の指標の値
Product_metrics = [[int(m) for m in input().split()] for n in range(N)]

# i番目の商品のポイント
Product_points = {}
for n in range(N):
    Product_points[n] = 0

for m in range(M):
    hoge = []
    for n in range(N):
        hoge.append(Product_metrics[n][m])

    count = 1
    same = 0
    while hoge != []:
        k = max(hoge)
        same = hoge.count(k) - 1
        while k in hoge:
            hoge.remove(k)
        for n in range(N):
            if k == Product_metrics[n][m]:
                Product_points[n] += N - count
        count += 1 + same

max_point = 0
for n in range(N):
    for key, values in Product_points.items():
        if max_point < values:
            max_point = values
            max_key = key
    print(max_key + 1)
    Product_points[max_key] = -1
    max_point = 0
