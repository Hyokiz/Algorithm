def solution(keyinput, board):
    curr_pos = [0, 0]
    mid_x, mid_y = board[0] // 2, board[1] // 2
    for i in keyinput:
        if i == "left":
            curr_pos[0] -= 1
        elif i == "right":
            curr_pos[0] += 1
        elif i == "down":
            curr_pos[1] -= 1
        else:
            curr_pos[1] += 1
        
        if curr_pos[0] < -mid_x:
            curr_pos[0] += 1
        elif curr_pos[0] > mid_x:
            curr_pos[0] -= 1
        elif curr_pos[1] < -mid_y:
            curr_pos[1] += 1
        elif curr_pos[1] > mid_y:
            curr_pos[1] -= 1
        
        print(curr_pos)
    
    return curr_pos