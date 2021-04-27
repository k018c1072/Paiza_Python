# 通常の時給 X、夜の時給 Y、深夜の時給 Z がこの順に整数
import pprint
X, Y, Z = [int(i) for i in input().split()]

# 出勤日数 N が整数
N = int(input())

# N 行の i 番目 (1 ≦ i ≦ N) には、i 日目の出勤時刻 S_i と退勤時刻 T_i がこの順に整数
Time = []
Time = [[int(i) for i in input().split()] for j in range(N)]

# 総給料
Total_salary = 0
for n in range(N):
    for t in range(Time[n][0], Time[n][1]):
        if t < 9:
            Total_salary += Z
        elif t < 17:
            Total_salary += X
        elif t < 22:
            Total_salary += Y
        else:
            Total_salary += Z

print(Total_salary)
