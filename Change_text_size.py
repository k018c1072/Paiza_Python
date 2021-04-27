H, W, X = [int(i) for i in input().split()]

Words = [[i for i in input()] for i in range(H)]
Words = sum(Words, [])

for i in range(0, H * W):
    if i % X == 0 and i != 0:
        print()
    print(Words[i], end="")
