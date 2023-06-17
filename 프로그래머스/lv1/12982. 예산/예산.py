def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        n = sum(d[:i+1])
        if budget < n:
            break
        answer += 1
    return answer