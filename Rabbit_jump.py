# N はしげみの個数を、M はうさぎの総数を、K はそれぞれのうさぎがジャンプする回数
N, M, K = [int(i) for i in input().split()]

# r_i は i 番目のうさぎがいるしげみの番号
r_position = {}
for n in range(1, N + 1):
    r_position[n] = 0
for m in range(1, M + 1):
    r_position[int(input())] = m


jump = 0
while (jump < K):
    number = set()
    for num, pos in r_position.items():
        if pos > 0 and not pos in number:
            i = 1
            n = num
            while True:
                if n + i > N:
                    n = 1
                    if r_position[n] == 0:
                        r_position[n] = pos
                        r_position[num] = 0
                        number.add(pos)
                        break
                elif r_position[n + i] == 0:
                    r_position[n + i] = pos
                    r_position[num] = 0
                    number.add(pos)
                    break
                else:
                    i += 1
    number.clear()
    jump += 1

for m in range(1, M + 1):
    for num, pos in r_position.items():
        if m == pos:
            print(num)
