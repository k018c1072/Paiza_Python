# チケットの枚数を表す N が整数
import pprint
N = int(input())

# 暗号チケットの指定された文字列 S
S = input()


# チケット
tickets = []
tickets = [input() for n in range(N)]

# 判定
Judgment = []
for t in tickets:
    if S == t:
        Judgment.append('valid')
    elif len(S) > len(t):
        Judgment.append('invalid')
    elif len(t) - len(S) == 1:
        count = 0
        tt = list(t)
        for s in list(S):
            for i in range(len(tt)):
                if s == tt[i]:
                    count += 1
                    tt[i] = '*'
                    break
        if count == len(S):
            Judgment.append('valid')
        else:
            Judgment.append('invalid')
    elif len(S) < len(t):
        check = False
        tt = list(t)
        num = len(t) - len(S)
        for i in range(num):
            count = 0
            pas = ''
            for s in range(len(S) + 1):
                pas += tt[s + i]
            p = list(pas)
            for s in list(S):
                for j in range(len(p)):
                    if s == p[j]:
                        count += 1
                        p[j] = '*'
                        break
            if count == len(S):
                check = True
            pas = ''
        if check:
            Judgment.append('valid')
        else:
            Judgment.append('invalid')
    else:
        Judgment.append('invalid')

for j in Judgment:
    print(j)
