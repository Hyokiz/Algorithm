def solution(answers):
    answer = []
    n1, n2, n3 = 0, 0, 0
    p1 = [1, 2, 3, 4, 5] 
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        m1 = i % 5
        m2 = i % 8
        m3 = i % 10
        
        if p1[m1] == answers[i]:
            n1 += 1
        
        if p2[m2] == answers[i]:
            n2 += 1
            
        if p3[m3] == answers[i]:
            n3 += 1
    
    max_n = max(n1, n2, n3)
    if n1 == max_n:
        answer.append(1)
    
    if n2 == max_n:
        answer.append(2)
        
    if n3 == max_n:
        answer.append(3)
    
    
    return answer