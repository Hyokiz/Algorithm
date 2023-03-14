# 2667. 단지번호붙이기

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# print(graph)
visited = [[False for _ in range(n)] for _ in range(n)]
dist = []
# 위에서부터 돌면서 dfs 로 방문
# 한번 방문한 곳의 길이를 측정 후 리스트에 저장
def out_of_range(x, y):
    return not(0 <= x < n and 0 <= y < n)

def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1

    for i, j in zip(dx, dy):
        nx, ny = x + i, y + j
        if out_of_range(nx, ny):
            continue

        if not visited[nx][ny] and graph[nx][ny]:
            dfs(nx, ny)


for r in range(n):
    for c in range(n):
        if not visited[r][c] and graph[r][c]:
            cnt = 0
            dfs(r, c)
            dist.append(cnt)
dist.sort()
print(len(dist))
for d in dist:
    print(d)