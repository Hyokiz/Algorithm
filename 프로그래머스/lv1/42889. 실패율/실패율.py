def solution(n, stages):
    res = dict()
    fail = len(stages)
    
    for i in range(1, n + 1):
        if fail != 0:
            cnt = stages.count(i)
            res[i] = cnt / fail
            fail -= cnt
        else:
            res[i] = 0
        
    return sorted(res, key = lambda x: res[x], reverse = True)