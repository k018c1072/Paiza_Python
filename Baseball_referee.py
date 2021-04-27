N = int(input())
s_count = 0
b_count = 0

for i in range(N):
    s = input()
    if s == "strike":
        s_count += 1
        if s_count == 3:
            print("out!")
        else:
            print("strike!")
    else:
        b_count += 1
        if b_count == 4:
            print("fourball!")
        else:
            print("ball!")
