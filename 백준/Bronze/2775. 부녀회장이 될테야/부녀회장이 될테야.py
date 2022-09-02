t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    apart = [[0] * 15 for _ in range(15)]

    # 1. 0층은 i호에는 i명
    cnt = 1
    for i in range(15):
        apart[0][i] += cnt
        cnt += 1

    # 2. 1호에는 1명
    for i in range(15):
        apart[i][0] = apart[0][0]

    # 3. 그 이후부터는 -1열과 -1행을 더해주면 된다.
    for i in range(1, 15):
        for j in range(1, 15):
            apart[i][j] = apart[i-1][j] + apart[i][j-1]

    print(apart[k][n-1])