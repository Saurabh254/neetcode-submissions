class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_mpp = {i: set() for i in range(len(board))}
        col_mpp = {i: set() for i in range(len(board[0]))}
        box_mpp = {i: set() for i in range(len(board))}

        for y in range(len(board)): 
            for x in range(len(board[0])): 
                if board[y][x] == '.': continue 
                box_idx = (y//3*3) + (x//3)

                if board[y][x] in row_mpp[y] or board[y][x] in col_mpp[x] or board[y][x] in box_mpp[box_idx]: 
                    return False  


                row_mpp[y].add(board[y][x])
                col_mpp[x].add(board[y][x])
                box_mpp[box_idx].add(board[y][x])



        return True


