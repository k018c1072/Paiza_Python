N = int(input())
H, W = (int(x) for x in input().split())

print((H * W) % N)
