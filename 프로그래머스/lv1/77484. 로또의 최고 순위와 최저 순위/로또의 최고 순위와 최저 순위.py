def solution(lottos, win_nums):
    answer = []
    rank = {
        2: 5, 3: 4, 4: 3,
        5: 2, 6: 1
    }
    cnt = 0
    zero = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            cnt += 1
    if cnt + zero < 2:
        answer.append(6)
    else:
        answer.append(rank[cnt + zero])
    if cnt < 2:
        answer.append(6)
    else:
        answer.append(rank[cnt])
    return answer