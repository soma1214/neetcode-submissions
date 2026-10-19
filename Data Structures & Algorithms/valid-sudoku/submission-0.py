class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        boxes=[[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                val=board[r][c]

                if val==".":
                    continue
                
                if val in row[r]:
                    return False
                row[r].add(val)

                if val in col[c]:
                    return False
                
                col[c].add(val)

                row_box=r//3
                col_box=c//3

                if val in boxes[row_box][col_box]:
                    return False
                
                boxes[row_box][col_box].add(val)
        return True