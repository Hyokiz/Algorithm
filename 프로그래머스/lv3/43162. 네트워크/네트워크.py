def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, n, visited, computers)
            answer += 1
    return answer

def dfs(x, n, visited, computers):
    visited[x] = True
    for j in range(n):
        if x == j:
            continue
        
        if computers[x][j] == 1 and not visited[j]:
            dfs(j, n, visited, computers)
        