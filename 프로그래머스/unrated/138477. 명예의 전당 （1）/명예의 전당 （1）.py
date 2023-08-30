def solution(k, score):
    answer = []
    li = []
    for i in range(len(score)):
        li.append(score[i])
        li = sorted(li, reverse = True)[:k]
        answer.append(min(li))
    return answer