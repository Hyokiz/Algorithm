# 1860. 진기의 최고급 붕어빵

for t in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort()    # 도착순 정렬

    total = 0
    for i in range(0, 11111 + 1):
        if i != 0 and i % m == 0:
            total += k
        # i초에 손님이 도착하는지 확인
        if i in times:
            if total <= 0:
                print(f'#{t} Impossible')
                break
            else:
                total -= 1
    else:
        print(f'#{t} Possible')   
                
            
        

