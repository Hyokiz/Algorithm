def solution(date1, date2):
    return int((date1[0] * 365 + date1[1] * 30 + date1[2]) < (date2[0] * 365 + date2[1] * 30 + date2[2]))