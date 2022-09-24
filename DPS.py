



sudoku = [list(map(int,input().split())) for _ in range(9)]
check = [[0]*9 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if sudoku[i][j] ==0:
            check[i][j] =1

while 1 in check:
    for i in range(9):
        for j in range(9):
             if check[i][j]==1:
                if sum(check[i])==1:
                    sudoku[i][j] = 45-sum(sudoku[i])
                    check[i][j] =0
                if sum([check[n][j] for n in range(9)]) ==1:
                    sudoku[i][j] = 45- sum([sudoku[m][j] for m in range(9)])
                    check[i][j] =0

for row in sudoku:
    print(row)
