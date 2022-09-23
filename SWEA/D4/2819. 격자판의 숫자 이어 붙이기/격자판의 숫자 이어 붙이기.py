dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, z):
    z += str(arr[x][y])
    if len(z) == 7:
        result.add(z)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, z)


for t in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, '')

    print(f'#{t}', len(result))