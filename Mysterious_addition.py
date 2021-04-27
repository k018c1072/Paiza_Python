# 足し算される PAIZA における数字を表す文字列 S_1, S_2
s_1, s_2 = [i for i in input().split()]


# 文字に対応する数字
num_dic = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}


# 5進数に変換
def Convert_to_quinary(s):
    hoge = list(s)
    num = []
    for i in hoge:
        for j in num_dic:
            if i == j:
                num.append(num_dic[j])
                break
    return num


# 10進数に変換
def Convert_to_decimal(hoge):
    length = len(hoge) - 1
    num = 0
    for i in hoge:
        num += i * (5 ** length)
        length -= 1
    return num


# 10進数から5進数に変換
def Convert_decimal_to_quinary(hoge):
    num = []
    while hoge > 5:
        i = hoge % 5
        hoge = hoge // 5
        num.append(i)
    num.append(hoge)
    return num


# 5進数から文字に変換
def Convert_quinary_to_character(hoge):
    char = []
    for i in hoge:
        for key, value in num_dic.items():
            if i == value:
                char.append(key)
                break
    return char


# 文字から5進数に
hoge_1 = Convert_to_quinary(s_1)
hoge_2 = Convert_to_quinary(s_2)

# 5進数から10進数に
hoge_1 = Convert_to_decimal(hoge_1)
hoge_2 = Convert_to_decimal(hoge_2)

# 10進数から5進数に
hoge = hoge_1 + hoge_2
hoge = Convert_decimal_to_quinary(hoge)

# 5進数から文字に
hoge = Convert_quinary_to_character(hoge)
for i in hoge:
    print(i, end="")
print()
