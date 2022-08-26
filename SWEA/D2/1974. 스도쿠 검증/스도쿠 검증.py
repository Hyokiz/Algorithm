def check(sudoku):
    # 1. 가로줄 검사
    for i in range(9):
        check_sudoku = []
        for j in range(9):
            if check_sudoku:
                if sudoku[i][j] in check_sudoku:
                    return 0
            check_sudoku.append(sudoku[i][j])

    # 2. 세로줄 검사
    for i in range(9):
        check_sudoku = []
        for j in range(9):
            if check_sudoku:
                if sudoku[j][i] in check_sudoku:
                    return 0
            check_sudoku.append(sudoku[j][i])

    # 3. 3*3 블록 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check_sudoku = []
            for k in range(3):
                for l in range(3):
                    if check_sudoku:
                        if sudoku[i+k][j+l] in check_sudoku:
                            return 0
                    check_sudoku.append(sudoku[i+k][j+l])
    return 1

for t in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t}', check(sudoku))
