# 社員の人数 n、グループの個数 g、および送られたメッセージの総数 m
import pprint
n, g, m = [int(i) for i in input().split()]

# グループ
group = {}
for i in range(g):
    group[str(i + 1)] = input().split()
    del group[str(i + 1)][0]

# メッセージ
mes = [[i for i in input().split()] for j in range(m)]

# 社員(Employee)
emp = {}
for i in range(n):
    emp[str(i + 1)] = ''

for i in range(m):
    if mes[i][1] != '0':
        for j in group[mes[i][1]]:
            emp[j] += mes[i][3] + '\n'
    else:
        emp[mes[i][0]] += mes[i][3] + '\n'
        emp[mes[i][2]] += mes[i][3] + '\n'

for k, v in emp.items():
    print(v, end="")
    if k != str(m):
        print('--')
