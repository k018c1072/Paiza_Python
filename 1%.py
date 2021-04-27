X = int(input())

# 預金
deposit = 100

count = 0
while deposit < X:
    deposit += deposit // 100
    count += 1

print(count)
