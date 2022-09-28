# 5521. 상원이의 생일파티
def dfs(i, n, c):
    if c == 3:
        return
    else:
        visited[i] = 1
        friend[i] = 1
        for j in range(1, n+1):
            if adjM[i][j] and visited[j] == 0:
                dfs(j, n, c+1)
        visited[i] = 0
        
        


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    adjM = [[0] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        adjM[a][b] = 1
        adjM[b][a] = 1
    visited = [0] * (n + 1)
    friend = [0] * (n + 1)
    dfs(1, n, 0)
    print(f'#{t}', sum(friend) - 1)

