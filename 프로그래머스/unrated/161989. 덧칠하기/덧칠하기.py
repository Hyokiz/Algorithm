def solution(n, m, section):
    answer = 0
    paint = set()
    for i in section:
        if i in paint:
            continue
        
        else:
            answer += 1
            for j in range(i, i + m):
                paint.add(j)

    return answer