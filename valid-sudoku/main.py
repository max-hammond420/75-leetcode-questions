class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        def check_rows(b):
            dict = {
                    (r, c): [] for r in range(3) for c in range(3)
            }
            for i in range(len(b)):
                ls = []
                for j in range(len(b[i])):
                    if b[i][j] != ".":
                        ls.append(b[i][j])
                        dict[(i//3, j//3)].append(b[i][j])
                if len(set(ls)) != len(ls):
                    return False
            print(dict)
            for v in dict.values():
                if len(set(v)) != len(v):
                    return False
            return True

        if check_rows(board) and check_rows(list(zip(*board))):
            return True
        
        return False

b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
for i in b:
    print(i)
print(Solution.isValidSudoku(Solution, b))
