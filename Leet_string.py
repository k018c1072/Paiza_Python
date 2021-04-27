s = input()
leet = {"A": "4", "E": "3", "G": "6", "I": "1", "O": "0", "S": "5", "Z": "2"}
After_conversion = []
for i in list(s):
    if i in leet:
        After_conversion.append(leet[i])
    else:
        After_conversion.append(i)

for i in After_conversion:
    print(i, end="")
