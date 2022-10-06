# 1948. 날짜 계산기
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, int(input()) + 1):
    start_m, start_d, end_m, end_d = map(int, input().split())
    result = 0
    for i in range(start_m + 1, end_m):
        result += days[i]

    if start_m != end_m:
        result += (days[start_m] - start_d) + end_d + 1
    else:
        result += end_d - start_d + 1

    print(f'#{t}', result)