def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

for _ in range(10):
    t, e = map(int, input().split())
    list_n = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [False] * 100
    print(f'#{t} ',end='')

    for i in range(0, e * 2, 2):
        graph[list_n[i]].append(list_n[i+1])

    dfs(0)
    if visited[99]:
        print('1')
    else:
        print('0')