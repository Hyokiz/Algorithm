# 1072. 게임

x, y = map(int, input().split())
win_rate = (100 * y) // x
l, r = 0, x
answer = x
if win_rate >= 99:
    answer = -1
else:
    while l <= r:
        m = (l + r) // 2
        if (100 * (y + m)) // (x + m) > win_rate:
            answer = m
            r = m - 1
        else:
            l = m + 1

print(answer)
