def solution(i, j, k):
    answer = 0
    li = list(map(str, range(i, j + 1)))
    for s in li:
        for u in s:
            if str(k) == u:
                answer += 1
    return answer