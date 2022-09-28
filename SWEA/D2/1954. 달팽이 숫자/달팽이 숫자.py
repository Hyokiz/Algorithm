for t in range(1, int(input())+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 우, 하, 좌, 상

    cnt = 1
    x, y = 0, 0
    nd = 0
    while cnt < n ** 2 + 1:

        arr[x][y] = cnt
        cnt += 1

        nx = x + dx[nd]
        ny = y + dy[nd]

        if (0 <= nx < n) and (0 <= ny < n) and not arr[nx][ny]:
            pass

        else:
            nd = (nd + 1) % 4

        x = x + dx[nd]
        y = y + dy[nd]

    print(f'#{t}')
    for i in range(n):
        print(*arr[i])