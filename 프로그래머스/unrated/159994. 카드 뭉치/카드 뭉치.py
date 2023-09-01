from collections import deque

def solution(cards1, cards2, goal):
    n = deque(cards1)
    m = deque(cards2)
    for i in goal:
        if n and n[0] == i:
            n.popleft()
        
        elif m and m[0] == i:
            m.popleft()
        
        else:
            return "No"
        
    return "Yes"