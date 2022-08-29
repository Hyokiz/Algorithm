# 우하좌상
dx1 = [0, 1, 0, -1]
dy1 = [1, 0, -1, 0]

# X자
dx2 = [1, 1, -1, -1] 
dy2 = [1, -1, -1, 1]
for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_value = 0
    for i in range(n):
        for j in range(n):
            cnt1 = arr[i][j]        # i, j를 중심으로 + 모양
            for k in range(4):
                for l in range(1, m):
                    nx, ny = i + dx1[k] * l, j + dy1[k] * l
                    if 0 <= nx < n and 0 <= ny < n:
                        cnt1 += arr[nx][ny]
            if max_value < cnt1:
                max_value = cnt1

            cnt2 = arr[i][j]
            for x in range(4):
                for y in range(1, m):
                    nx, ny = nx, ny = i + dx2[x] * y, j + dy2[x] * y
                    if 0 <= nx < n and 0 <= ny < n:
                        cnt2 += arr[nx][ny]
            if max_value < cnt2:
                max_value = cnt2

    print(f'#{t} {max_value}')