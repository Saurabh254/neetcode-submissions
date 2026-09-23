class Solution:
    def validateTheIndex(self, board: list[list[str]], x: int, y: int): 
        value = board[y][x]
        if value == '.': return True

        # x axis 
        for i in range(len(board[0])): 
            if value == board[y][i] and x != i: 
                return False

        # y axis 
        for i in range(len(board)): 
            if value == board[i][x] and i != y: return False
        
        box_start_left = x//3*3
        box_start_top = y//3*3
        seen = set()
        for i in range(box_start_top, 3+box_start_top): 
            for j in range(box_start_left, 3+box_start_left):
                if board[i][j] == '.': 
                    continue 
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(len(board)): # y axis
            for x in range(len(board[0])): # x axis
                if not self.validateTheIndex(board, x, y): 
                    return False
        return True 

        