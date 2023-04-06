def solution(s):
    flag = 0
    for i in s:
        if i == "(":
            flag += 1

        else:
            if not flag:
                return False
            else:
                flag -= 1
    
    if not flag:
        return True
    else:
        return False