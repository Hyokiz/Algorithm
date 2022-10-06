# 1940. 가랏! RC카!

for t in range(1, int(input()) + 1):
    n = int(input())
    dist = 0
    speed = 0
    for _ in range(n):
        info = list(map(int, input().split()))
        if info[0] == 1:
            speed += info[1]
        elif info[0] == 2:
            if speed < info[1]:
                speed = 0
            else:
                speed -= info[1]
        
        dist += speed
    
    print(f'#{t}', dist)