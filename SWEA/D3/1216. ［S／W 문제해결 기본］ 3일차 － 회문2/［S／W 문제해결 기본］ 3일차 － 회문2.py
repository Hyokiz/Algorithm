for _ in range(10):

    t = int(input())
    print(f'#{t}', end=" ")
    arr = [list(map(str, input())) for _ in range(100)] # 입력 배열
    z_arr = list(zip(*arr)) # 세로줄 검사용 zip 배열
    result = 1
    for k in range(100, 1, -1):
        for i in range(100): # 가로줄 검사
            cnt = 0
            for j in range(100 - k + 1):

                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    cnt = len(arr[i][j:j+k])

                if result < cnt: # result 갱신
                    result = cnt

        for i in range(100): # 세로줄 검사
            for j in range(100 - k + 1):
                if z_arr[i][j:j+k] == z_arr[i][j:j+k][::-1]:
                    cnt = len(arr[i][j:j+k])

                if result < cnt: # result 갱신
                    result = cnt

    print(result)