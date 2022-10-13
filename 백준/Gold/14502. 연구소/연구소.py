# 14502. 연구소
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def is_out_of_range(x, y):
    return not(0 <= x < n and 0 <= y < m)


def bfs():
    new_arr = deepcopy(arr)
    queue = deque()

    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j

            if is_out_of_range(nx, ny):
                continue

            if new_arr[nx][ny] == 0:
                new_arr[nx][ny] = 2
                queue.append((nx, ny))

    global ans
    cnt = 0

    for i in range(n):
        cnt += new_arr[i].count(0)

    ans = max(ans, cnt)


def backtracking(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                backtracking(cnt+1)
                arr[i][j] = 0


backtracking(0)
print(ans)