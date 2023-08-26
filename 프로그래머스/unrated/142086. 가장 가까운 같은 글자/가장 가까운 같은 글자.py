def solution(s):
    answer = []
    for i in range(len(s) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if s[i] == s[j]:
                answer.append(abs(j - i))
                break
        else:
            answer.append(-1)
    answer.append(-1)
                
    return answer[::-1]