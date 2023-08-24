def solution(arr, n):
    m = len(arr)
    if m % 2 == 1:
        for i in range(0, m, 2):
            arr[i] += n
    else:
        for i in range(1, m, 2):
            arr[i] += n
    return arr
    
    