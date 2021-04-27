Current = [int(i) for i in input().split()]
N = int(input())

Evolution = [[i for i in input().split()] for j in range(N)]
Evolved_monster = []

for i in Evolution:
    if Current[0] >= int(i[1]) and int(i[2]) >= Current[0]:
        if Current[1] >= int(i[3]) and int(i[4]) >= Current[1]:
            if Current[2] >= int(i[5]) and int(i[6]) >= Current[2]:
                Evolved_monster.append(i[0])

if not Evolved_monster:
    print("no evolution")
else:
    for i in Evolved_monster:
        print(i)
