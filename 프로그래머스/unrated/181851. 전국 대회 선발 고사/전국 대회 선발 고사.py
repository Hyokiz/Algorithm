def solution(rank, attendance):
    answer = []
    for i in range(1, len(rank) + 1):
        if len(answer) == 3:
            break
        
        if attendance[rank.index(i)]:
            answer.append(rank.index(i))

    return 10000 * answer[0] + 100 * answer[1] + answer[2]
        