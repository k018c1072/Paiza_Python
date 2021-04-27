N = int(input())

word = []
check = ["a", "i", "u", "e", "o"]
y_check = True
Mul = ""  # 複数 Multiple
for i in range(N):
    Sin = input()  # Singular…単数
    if (Sin[-1] == "s" or Sin[-2:] == "sh" or Sin[-2:] == "ch" or Sin[-1] == "o" or Sin[-1] == "x"):
        Mul += "es"
    elif (Sin[-1] == "f"):
        Mul = Sin[:-1] + "ves"
    elif (Sin[-2:] == "fe"):
        Mul = Sin[:-2] + "ves"
    elif (Sin[-1] == "y"):
        for c in check:
            if (Sin[-2] == c):
                y_check = False
        if (y_check == False):
            Mul = Sin + "s"
        else:
            Mul = Sin[:-1] + "ies"
    else:
        Mul = Sin + "s"
    word.append(Mul)

for i in range(N):
    print(word[i])
