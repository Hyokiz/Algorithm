def solution(keymap, targets):
    answer = []
    
    for target in targets:
        total = 0
        
        for char in target:
            flag = False
            time = 101
            
            for key in keymap:
                if char in key:
                    time = min(key.index(char) + 1, time)
                    flag = True
            
            if not flag:
                total = -1
                break
                
            total += time
        
        answer.append(total)
    
    return answer