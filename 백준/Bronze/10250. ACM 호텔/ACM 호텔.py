t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    hotel = [[0] * w for _ in range(h)]

    cnt = 1
    for j in range(w):
        for i in range(h-1, -1, -1):
            hotel[i][j] += cnt
            cnt += 1

    result = ''
    for i in range(h):
        for j in range(w):
            if hotel[i][j] == n:
                if len(str(j+1)) == 1:
                    result += str(h - i) + '0' + str(j + 1)
                else:
                    result += str(h - i) + str(j + 1)

    print(result)