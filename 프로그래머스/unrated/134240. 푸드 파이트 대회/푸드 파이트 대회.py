def solution(food):
    answer = ''
    for i in range(len(food)):
        if food[i] < 2:
            food[i] = 0
            continue
        food[i] //= 2
    
    for idx, val in enumerate(food):
        if val == 0:
            continue
        answer += str(idx) * val
    
    return answer + "0" + answer[::-1]