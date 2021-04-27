import math

# 配座駅へまで時間 toP 分, 配座駅から儀野駅の乗車時間 toG 分, 儀野駅から会社までの時間 toC 分
toP, toG, toC = [int(i) for i in input().split()]

# 配座駅から出る電車の本数を表す整数 N
N = int(input())

# n本目の電車の発車時刻 h_1 時 m_1 分
Electric_train = []
for n in range(N):
    Electric_train.append([int(t) for t in input().split()])

# 合計移動時間
Travel_time = toG + toC

for n in range(N):
    time = Electric_train[n][1] + Travel_time
    hh = Electric_train[n][0] + math.floor(time / 60)
    mm = time % 60
    if hh < 9:
        Latest = n

if Electric_train[Latest][1] < toP:
    h = Electric_train[Latest][0] - 1
    m = 60 - (toP - Electric_train[Latest][1])
else:
    h = Electric_train[Latest][0]
    m = Electric_train[Latest][1] - toP

h = "0" + str(h)
if m / 10 < 1:
    m = "0" + str(m)
else:
    m = str(m)
print(h + ":" + m)
