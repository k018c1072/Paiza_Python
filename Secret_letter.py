ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
       "N", "O", "P", "Q", "R",  "S",  "T", "U", "V", "W", "X", "Y", "Z"]

N = int(input())
S = input()

for i in range(len(S)):
    for j in range(len(ABC)):
        if S[i] == ABC[j]:
            count = j
    if i % 2 == 0:
        angou = count - N
        if angou < 0:
            angou = 26 + angou
    else:
        angou = count + N
        if angou > 25:
            angou = angou - 26
    print(ABC[angou], end="")
