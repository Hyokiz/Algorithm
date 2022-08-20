for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    # 1. 파리채 반복
    for row in range(n - m + 1):
        for col in range(n - m + 1):
            cnt = 0 # 한 번 잡았을 경우 파리
            # 2. 파리채 내부 숫자 더하기
            for i in range(m):
                for j in range(m):
                    cnt += board[row + i][col + j]
            
            if result < cnt:
                result = cnt

    print(f'#{t} {result}')