# タクシーの種類数 N、目的地までの距離 X
N, X = [int(i) for i in input().split()]

# タクシーの 初乗り距離 a_i、 初乗り運賃 b_i、 加算距離 c_i、 加算運賃 d_i
Taxi = [[int(i) for i in input().split()] for n in range(N)]

min_fare = 0
max_fare = 0

for n in range(N):
    distance = X - Taxi[n][0]
    fare = Taxi[n][1]
    if distance == 0:
        fare += Taxi[n][3]
    else:
        while distance >= 0:
            fare += Taxi[n][3]
            distance -= Taxi[n][2]
    if min_fare == 0:
        min_fare = fare
    elif min_fare > fare:
        min_fare = fare
    if max_fare == 0:
        max_fare = fare
    elif max_fare < fare:
        max_fare = fare

print(str(min_fare) + " " + str(max_fare))
