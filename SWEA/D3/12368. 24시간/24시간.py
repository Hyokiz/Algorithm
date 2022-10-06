# 12368. 24시간

for t in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    result = (a + b) % 24
    print(f'#{t}', result)