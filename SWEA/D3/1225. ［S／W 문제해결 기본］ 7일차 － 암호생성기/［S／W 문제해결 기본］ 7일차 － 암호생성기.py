for _ in range(10):
    t = int(input())
    q = list(map(int, input().split()))

    # q[-1]이 0일때까지 반복
    while q[-1] != 0:
        # 1~5까지 감소
        for i in range(1, 6):
            new_q = q[0] - i
            q = q[1:]
            q.append(new_q)
            # 마지막 숫자가 0이하일때 0으로 만들어주고 탈출
            if new_q <= 0:
                q[-1] = 0
                break

    print(f'#{t}', *q)