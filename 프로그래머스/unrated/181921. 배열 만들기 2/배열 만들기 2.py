def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if i % 5 == 0:
            
            if not str(i).replace("5", "").replace("0", ""):
                answer.append(i)
    return answer if answer else [-1]