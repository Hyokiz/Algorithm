def solution(n):
    answer = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(1 if i == j else 0)
        answer.append(temp)
    return answer