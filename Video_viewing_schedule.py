# 期間内の全ての動画の数を表す整数 N
import pprint
N = int(input())

# N 行のうちの i 行目 (1 ≦ i ≦ N) には、それぞれ i 番目の動画の開始時間と
# 動画の長さを表す整数 s_i, p_iがこの順で半角スペース区切りで与えられます。
videos = {}
for n in range(N):
    start, time = [int(j) for j in input().split()]
    videos[n + 1] = {'start': start, 'time': time, 'end': start + time}

pprint.pprint(videos)


# 視聴
def viewing(now):
    global end_time
    end_time = videos[now]['end']


start_time = 0
cnt = 0
max = 0
for n in range(1, N):
    start_time = videos[n]['start']
    end_time = videos[n]['end']
    # 次観る動画で一番早く始まり、終わるのを見つける
    for i in range(n + 1, N):
        end_time = videos[n]['end']
        for j in range(i, N):
            if end_time < videos[j]['start']:
                viewing(j)
                cnt += 1
        if max < cnt:
            max = cnt
        cnt = 0
    print(max)

print(max)
