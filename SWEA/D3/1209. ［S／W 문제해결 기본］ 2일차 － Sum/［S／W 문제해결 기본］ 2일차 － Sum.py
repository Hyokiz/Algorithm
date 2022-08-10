for t in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxV = 0
    for i in range(100):

        # 가로 합
        row = 0
        for j in range(100):
            row += arr[i][j]

            if maxV < row:
                maxV = row

        # 세로 합
        col = 0
        for j in range(100):
            col += arr[j][i]

            if maxV < col:
                maxV = col

        # 좌측 대각선
        left_arrow = 0
        for i in range(100):
            left_arrow += arr[i][i]

            if maxV < left_arrow:
                maxV = left_arrow

        # 우측 대각선
        right_arrow = 0
        for i in range(100):
            right_arrow += arr[i][100-i-1]

            if maxV < right_arrow:
                maxV = right_arrow

    print(f'#{t} {maxV}')