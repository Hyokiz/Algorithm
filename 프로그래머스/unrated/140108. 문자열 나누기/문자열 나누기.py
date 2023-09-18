def solution(s):
    answer = 0
    words = []
    x, y, si, ei, sw = 0, 0, 0, 0, ""
    for i in range(len(s)):
        if sw == "":
            sw = s[i]
            si = i
        
        if sw == s[i]:
            x += 1
        else:
            y += 1
        
        if x == y:
            ei = i
            words.append(s[si:ei+1])
            x, y, si, ei, sw = 0, 0, 0, 0, ""
    
    if sw:
        words.append(sw)
    
    return len(words)