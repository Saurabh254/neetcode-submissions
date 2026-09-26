class Solution:

    def isValidNumber(self, board: list[list[str]], row: int , col: int) -> bool:
        if board[row][col] == '.': return True

        # check for all the col

        for idx in range(len(board[0])):
            if idx != col and board[row][idx] == board[row][col]: 
                return False
        
        # check for all the rows 
        for idx in range(len(board)): 
            if idx != row and board[idx][col] == board[row][col]: 
                return False

        # check if the element is not present on the 3x3
        start_box_top = (row//3) * 3
        start_box_left = (col//3) * 3

        for box_row in range(start_box_top, start_box_top+3): 
            for box_col in range(start_box_left, start_box_left+3): 
                if box_row != row and box_col != col and board[row][col] == board[box_row][box_col]: 
                    return False  
        return True 
        
        
         

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(len(board)): 
            for col in range(len(board[0])): 
                if not self.isValidNumber(board, row, col): 
                    return False
        return True 
        