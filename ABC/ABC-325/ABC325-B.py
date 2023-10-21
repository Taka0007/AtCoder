N = int(input())
times = []
for _ in range(N):
    times.append(list(map(int, input().split())))


# 時間を全探索
people_lis = []
for time in range(0,25):
    people = 0
    for i in range(N):
        if (times[i][1] + time) %24 <= 17 and (times[i][1] + time) %24 >= 9:
            people += times[i][0]
            people_lis.append(people)
print(max(people_lis))