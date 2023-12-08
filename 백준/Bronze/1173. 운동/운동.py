N, m, M, T, R = map(int, input().split())   # N = 운동시간, m = 초기맥박, M = 최대맥박, T = 맥박증가, R = 맥박감소

pulse = m
time = 0
exercise = 0

while exercise < N:
    if m + T > M:
        time = -1
        break

    time += 1
    if pulse + T <= M:
        pulse += T
        exercise += 1
    else:
        if pulse - R < m:
            pulse = m
        else:
            pulse -= R

print(time)