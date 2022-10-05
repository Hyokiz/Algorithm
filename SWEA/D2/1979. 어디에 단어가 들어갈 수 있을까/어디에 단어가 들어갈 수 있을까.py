# 1979. 어디에 단어가 들어갈 수 있을까

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for r in range(n):
        cnt = 0
        for c in range(n):
            if arr[r][c] == 1:
                cnt += 1

            if arr[r][c] == 0 or c == n-1:
                if cnt == k:
                    result += 1
                cnt = 0

        for c in range(n):
            if arr[c][r] == 1:
                cnt += 1

            if arr[c][r] == 0 or c == n-1:
                if cnt == k:
                    result += 1
                cnt = 0

    print(f'#{t}', result)