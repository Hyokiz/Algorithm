# 15612. 체스판 위의 룩 배치

for t in range(1, int(input()) + 1):
    chess = [list(input()) for _ in range(8)]
    col = [0] * 8
    cnt = 0
    ans = False
    flag = False
    for i in range(8):
        if chess[i].count('O') == 1:
            cnt += 1

    if cnt == 8:
        for i in range(8):
            for j in range(8):
                if chess[i][j] == 'O':
                    if col[j]:
                        flag = True
                        break
                    else:
                        col[j] = 1
            if flag:
                break

    if sum(col) == 8:
        ans = True

    if ans:
        print(f'#{t} yes')
    else:
        print(f'#{t} no')