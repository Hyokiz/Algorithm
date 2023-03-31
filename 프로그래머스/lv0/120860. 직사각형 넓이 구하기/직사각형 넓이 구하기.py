def solution(dots):
    answer = 0
    curr_x, curr_y = dots[0][0], dots[0][1]
    row, col = 0, 0
    for i in range(1, 4):
        next_x, next_y = dots[i][0], dots[i][1]
        if next_x == curr_x and next_y != curr_y:
            row = abs(next_y - curr_y)
        elif next_y == curr_y and next_x != curr_x:
            col = abs(next_x - curr_x)
        
        if row and col:
            break
            
            
    return row * col