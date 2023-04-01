def solution(lines):
    answer = 0
    cnt = [0] * 201
    for i in lines:
        s, e = i[0], i[1]
        for j in range(s + 100, e + 100):
            cnt[j] += 1
    
    for n in range(201):
        if cnt[n] >= 2:
            answer += 1
        
    return answer