# N回だけトレーニングする
import numpy as np
N = int(input())

# パワー
power = 1

# i回目のトレーニングを終えるとパワーが
# i倍されます。
# 答えの値は非常に大きな値になることがあるので
# 10**9+7で割ったあまりを出力

for i in range(1, N + 1):
    power = np.mod(i * power, 10 ** 9 + 7)
print(power)
