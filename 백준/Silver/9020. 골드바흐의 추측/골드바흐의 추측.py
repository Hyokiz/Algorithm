dp = [False, False] + [True] * 10000
for i in range(2, 101):
    if dp[i]:
        for j in range(i+i, 10001, i):
            dp[j] = False

t = int(input())
for _ in range(t):
    n = int(input())

    s = n // 2
    e = s
    for _ in range(10000):
        if dp[s] and dp[e]:
            print(s, e)
            break

        s -= 1
        e += 1