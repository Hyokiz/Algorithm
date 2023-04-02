def solution(s):
    cnt_p, cnt_y = s.count("p"), s.count("y")
    cnt_p += s.count("P")
    cnt_y += s.count("Y")
    if cnt_p == cnt_y:
        return True
    else:
        return False
    