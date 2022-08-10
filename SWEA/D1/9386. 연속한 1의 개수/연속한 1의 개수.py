t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input()))
    cnt = 0
    maxV = 0
    for i in range(n):
        if arr[i] == 1:
            cnt += 1
            if maxV < cnt:
                maxV = cnt
        else:
            cnt = 0
    print(f'#{tc} {maxV}')

    
#t = int(input())

#for tc in range(1, t+1):
#    n = int(input())
#    arr = list(map(int, input()))
#    maxV = 0
#    for i in range(n):
#        arr[i] = arr[i-1] * arr[i] + arr[i]
#
#        if maxV < arr[i]:
#            maxV = arr[i]
#
#    print(f'#{tc} {maxV}')