def solution(num):
    max_value = 500
    cnt = 0
    while max_value > 0:
        if num == 1:
            return cnt
        
        max_value -= 1
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        cnt += 1
    return -1