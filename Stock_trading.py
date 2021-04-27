"""
*条件
あなたは、株の売買でのお金儲けを考えています。
N 日の間、1 日に一度株価をチェックし、以下のルールに従い売買をします。

・株価が c_1 円以下の場合、1 株買う
・株価が c_2 円以上の場合、持ち株すべて売る
・株価が c_1 円、c_2 円の間の場合は、何もしない
・N 日目には、上記を行わず持ち株をすべて売る
"""

# 株の売買を行う日数表す整数 N、株の売買条件を表す整数 c_1, c_2
N, c_1, c_2 = [int(i) for i in input().split()]

# 株価
Stock_price = []
for i in range(N):
    Stock_price.append(int(input()))

# 利益
profit = 0

# 株
stock = 0

# 売買
for i in range(N):
    if i + 1 == N:
        if stock != 0:
            profit += Stock_price[i] * stock
            break
        else:
            break
    elif Stock_price[i] <= c_1:
        profit -= Stock_price[i]
        stock += 1
    elif Stock_price[i] >= c_2:
        profit += Stock_price[i] * stock
        stock = 0

print(profit)
