def solution(arr):
    answer = 0
    while True:
        cnt = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] >= 50:
                arr[i] //= 2
                cnt += 1
            elif arr[i] % 2 == 1 and arr[i] < 50:
                arr[i] = arr[i] * 2 + 1
                cnt += 1
        
        if cnt == 0:
            break
        else:
            answer += 1
    return answer