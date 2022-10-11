# 1085. 직사각형에서 탈출

x, y, w, h = map(int, input().split())
print(min((x-0), (y-0), abs(x-w), abs(y-h)))