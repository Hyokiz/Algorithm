def solution(s):
    answer = ''
    ls = set(map(int, s.split(" ")))    
    if len(ls) == 1:
        return f'{max(ls)} {max(ls)}'
    else:
        return f'{min(ls)} {max(ls)}'