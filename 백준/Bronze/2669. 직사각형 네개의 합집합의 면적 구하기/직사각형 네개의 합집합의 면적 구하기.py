arr = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(4):
    start_x, start_y, end_x, end_y = map(int, input().split())
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            arr[i][j] += 1

for i in range(100):
    for j in range(100):
        if arr[i][j] != 0:
            cnt += 1

print(cnt)