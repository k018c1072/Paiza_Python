# 生成手順を繰り返す回数を表す整数 K
K = int(input())

# 最初に与えられる正方形の辺の長さを表す整数 N
N = int(input())

# N 行のうちの i 行目 (1 ≦ i ≦ N) には、
# 半角記号 "#" および "." からなる長さ N の文字列 si が与えられます。
# si の j 番目 (1 ≦ j ≦ N) の文字は初期状態における上から i 番目、
# 左から j 番目の正方形の色に対応しており、"#" は水色を、"." は白色を表します。
pattern = [[p for p in list(input())] for n in range(N)]


def c_length(pattern):
    return len(pattern)


def c_width(pattern):
    return len(pattern[0])


count = 0
while K > count:

    pattern_b = pattern.copy()
    pattern = [[0 for i in range(c_width(pattern) * c_width(pattern))]
               for j in range(c_length(pattern) * c_length(pattern))]

    a = 0
    b = 0

    for i in range(c_length(pattern_b)):
        if i > 0:
            a += c_length(pattern_b)
            b = 0
        for j in range(c_width(pattern_b)):
            if j > 0:
                b += c_width(pattern_b)
            if pattern_b[i][j] == "#":
                for l in range(c_length(pattern_b)):
                    for w in range(c_width(pattern_b)):
                        pattern[a + l][b + w] = pattern_b[l][w]
            else:
                for l in range(c_length(pattern_b)):
                    for w in range(c_width(pattern_b)):
                        pattern[a + l][b + w] = "."
    count += 1

for i in range(c_length(pattern)):
    for j in range(c_width(pattern)):
        print(pattern[i][j], end="")
    print()
