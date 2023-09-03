def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    for i in range(0, len(score), m):
        li = score[i:i+m]
        if len(li) < m:
            continue
        
        answer += (min(li) * m)
        
    return answer