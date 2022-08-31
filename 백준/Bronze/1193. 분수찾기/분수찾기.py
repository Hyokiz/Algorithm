x = int(input())

line = 1
while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    up_num = x
    down_num = line - x + 1
else:
    up_num = line - x + 1
    down_num = x

print(up_num, '/', down_num, sep='')