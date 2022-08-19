def dfs(x):
    visited[x] = True
    for next_x in graph[x]:
        if not visited[next_x]:
            dfs(next_x)


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for i in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            cnt += 1
            dfs(i)

    print(f'#{t} {cnt}')