# 1865. 동철이의 일 분배
def dfs(worker, cnt):
    global max_value, n
    if cnt <= max_value:
        return

    if worker == n:
        if cnt > max_value:
            max_value = cnt
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(worker + 1, cnt * percent[worker][i] / 100)
            visited[i] = False


for t in range(1, int(input()) + 1):
    n = int(input())
    percent = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    max_value = 0
    dfs(0, 1)
    print(f'#{t} {max_value*100:.6f}')