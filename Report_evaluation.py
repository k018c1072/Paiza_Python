# 1 行目に学生の人数を表す整数 k、レポートの問題数を表す整数 n
import math
import pprint
k, n = [int(i) for i in input().split()]

# 一問あたりの点数
score = 100 / n
# 提出日
Filing_date = []
# 問題
problem = []
# 評価
evaluation = []

for i in range(k):
    f, p = [int(j) for j in input().split()]
    Filing_date.append(f)
    problem.append(p)

for i in range(k):
    if Filing_date[i] <= 0:
        s = problem[i] * score
    elif Filing_date[i] <= 9:
        s = math.floor((problem[i] * score) * 0.8)
    else:
        s = 0

    if s >= 80:
        evaluation.append("A")
    elif s >= 70:
        evaluation.append("B")
    elif s >= 60:
        evaluation.append("C")
    else:
        evaluation.append("D")

for i in range(k):
    print(evaluation[i])
