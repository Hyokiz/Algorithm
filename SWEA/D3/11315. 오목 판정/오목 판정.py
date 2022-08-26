# def check(omok):
#     # 1. 가로줄 검사
#     cnt = 1
#     for i in range(n):
#         for j in range(n-1):
#             if omok[i][j] == omok[i][j+1] == 'o':
#                 cnt += 1
#
#     if cnt >= 5:
#         return "YES"
#
#     # 2. 세로줄 검사
#     cnt = 1
#     for i in range(n):
#         for j in range(n-1):
#             if omok[j][i] == omok[j+1][i] == 'o':
#                 cnt += 1
#
#     if cnt >= 5:
#         return "YES"
#
#     # 3. 대각선 검사
#     left_li = []
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 left_li.append(omok[i][j])
#
#     l_cnt = 1
#     for k in range(len(left_li)-1):
#         if left_li[k] == left_li[k+1] == 'o':
#             l_cnt += 1
#
#     if l_cnt >= 5:
#         return "YES"
#
#     right_li = []
#     for i in range(n):
#         for j in range(n-1, -1, -1):
#             if i == n-1-j:
#                 right_li.append(omok[i][j])
#
#     r_cnt = 1
#     for k in range(len(right_li) - 1):
#         if right_li[k] == right_li[k+1] == 'o':
#             r_cnt += 1
#
#     if r_cnt >= 5:
#         return "YES"
#
#     return "NO"
#
# for t in range(1, int(input()) + 1):
#     n = int(input())
#     omok = [list(map(str, input())) for _ in range(n)]
#
#     print(f'#{t} {check(omok)}')

# 하 우 좌하 우하
dx = [1, 0, 1, 1]
dy = [0, 1, -1, 1]

def check(omok):

    for x in range(n):
        for y in range(n):
            if omok[x][y] == 'o':
                for z in range(4):
                    nx = x
                    ny = y
                    cnt = 0
                    while 0 <= nx < n and 0 <= ny < n and omok[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[z]
                        ny += dy[z]

                    if cnt >= 5:
                        return "YES"

    return "NO"

for t in range(1, int(input()) + 1):
    n = int(input())
    omok = [list(map(str, input())) for _ in range(n)]
    print(f'#{t} {check(omok)}')