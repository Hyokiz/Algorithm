# 13547. 팔씨름

for t in range(1, int(input()) + 1):
    games = list(input())
    # 결과
    result = True

    if games.count('x') >= 8:
        result = False

    if result:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')