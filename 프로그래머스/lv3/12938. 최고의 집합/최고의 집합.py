def solution(n, s):
    answer = []
    while True:
        if n == 1:
            answer.append(s)
            break
            
        m = s // n
        answer.append(m)
        s -= m
        n -= 1

    answer.sort()
    if 0 in answer:
        return [-1]
    return answer