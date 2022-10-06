for t in range(1, int(input()) + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    result = 0
    
    # 가장 마지막 날 값을 max_value로 잡는다.
    max_value = prices[-1]

    # 가장 마지막 날 값보다 전날 값이 더 크다면 갱신해준다.
    # 이득은 result에 더한다.
    # 마지막 날 가격 < 그 전날 가격 이라면 손해를 보기 때문
    # 최대 이익을 보려면 가장 비쌀때 팔아야 한다.
    
    for i in range(n-1, -1, -1):
        if prices[i] > max_value:
            max_value = prices[i]
        result += max_value - prices[i]

    print(f'#{t}', result)