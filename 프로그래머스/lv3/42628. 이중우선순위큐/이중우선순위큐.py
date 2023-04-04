from collections import deque

def solution(operations):
    answer = []
    q = deque([])
    for i in operations:
        com, val = i.split(" ")
        val = int(val)
        
        # 1. I일 경우
        if com == "I":
            q.append(val)
        # 2. E일 경우
        else:
            # 2-1. 큐가 비어있을 경우
            if not q:
                continue
            # 2-2. 큐가 비어있지 않을 경우
            else:
                # a. 최댓값 삭제
                if val == 1:
                    q.remove(max(q))
                # b. 최솟갑 삭제
                else:
                    q.remove(min(q))
                
    if q:
        return [max(q), min(q)]
    else:
        return [0, 0]