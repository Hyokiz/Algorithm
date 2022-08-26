for t in range(1, int(input()) + 1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    result = 0
    # 시작점과 끝점 행의 가운데로 잡는다.
    start, end = n//2, n//2
    for i in range(n):
        for j in range(start, end + 1):
            result += farm[i][j]
        # 행이 중간을 넘지 않는 경우 start와 end의 간격을 한칸씩 벌린다.
        if i < n//2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print(f'#{t} {result}')