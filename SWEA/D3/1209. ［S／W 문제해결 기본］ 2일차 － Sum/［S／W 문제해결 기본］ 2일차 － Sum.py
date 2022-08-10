for t in range(10): # 문제에서 10개라고 정의.
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)] # 2차원 리스트 생성

    maxV = 0 # 한번 돌 때 마다 maxV 값 초기화
    for i in range(100):

        # 가로(행) 합
        row = 0
        for j in range(100):
            row += arr[i][j]

            if maxV < row:
                maxV = row

        # 세로(열) 합
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