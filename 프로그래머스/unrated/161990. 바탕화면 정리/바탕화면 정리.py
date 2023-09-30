import sys

def solution(wallpaper):
    rs, cs = set(), set()
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[row])):
            if wallpaper[row][col] == "#":
                rs.add(row)
                cs.add(col)
    
    return [min(rs), min(cs), max(rs) + 1, max(cs) + 1]