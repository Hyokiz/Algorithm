def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        move -= 1
        for row in range(len(board)):
            temp = board[row][move]
            
            if temp != 0:
                if stack and stack[-1] == temp:
                    answer += 2
                    stack.pop()
                    board[row][move] = 0
                    break
                else:
                    stack.append(temp)
                    board[row][move] = 0
                    break
                
            
    return answer