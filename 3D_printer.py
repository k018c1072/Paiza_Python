# X は立体の奥行き(二次元配列では列)を、Y は立体の横幅(二次元配列では行)を、Z は立体の高さを表す整数です。
import pprint
X, Y, Z = [int(i) for i in input().split()]

# Three-dimensional...立体
td = [[[0 for y in range(Y)]for x in range(X)] for z in range(Z)]

for z in range(Z):
    for x in range(X + 1):
        data = input()
        if data != "--":
            y = 0
            for cell in list(data):
                td[x][y][z] = cell
                y += 1

# Plane...平面
plane = [["." for y in range(Y)] for z in range(Z)]
for z in range(Z):
    for y in range(Y):
        for x in range(X):
            if td[x][y][z] == "#":
                plane[z][y] = "#"

plane.reverse()
for z in range(Z):
    for y in range(Y):
        print(plane[z][y], end="")
    print()
