paper = [[0] * 100 for _ in range(100)]
cnt = 0
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            if paper[i][j] != 0:
                cnt += 1
            paper[i][j] = 1

print(100 * n - cnt)