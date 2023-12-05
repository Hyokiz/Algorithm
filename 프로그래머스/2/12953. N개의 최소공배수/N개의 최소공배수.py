def solution(arr):
    n = max(arr)
    answer = n
    while True:
        for i in arr:
            if answer % i != 0:
                break
        else:
            break
        
        answer += n
    return answer