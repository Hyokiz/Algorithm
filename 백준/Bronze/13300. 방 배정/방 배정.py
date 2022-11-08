from math import ceil
n, k = map(int, input().split())
graph = [[0, 0] for _ in range(7)]
for _ in range(n):
    s, y = map(int, input().split())
    if s == 1:
        graph[y][1] += 1
    else:
        graph[y][0] += 1

r = 0
for i in range(1, 7):
    for j in range(2):
        r += ceil(graph[i][j] / k)

print(r)