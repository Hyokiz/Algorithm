# 1976. 시각 덧셈

for t in range(1, int(input()) + 1):
    times = list(map(int, input().split()))
    hour, minute = 0, 0
    for i in range(0, 4, 2):
        h, m = times[i], times[i+1]
        hour += h
        minute += m

    if minute > 60:
        hour += 1
        minute -= 60

    if hour > 12:
        hour -= 12

    print(f'#{t}', hour, minute)