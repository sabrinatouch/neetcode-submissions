class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_dict = {}
        for i in range(0, 9):
            for j in range (0, 9):
                if board[i][j] not in row_dict:
                    row_dict[board[i][j]] = 1
                elif board[i][j] != '.':
                    row_dict[board[i][j]] += 1
            #print(row_dict.values())
            for value in row_dict.values():
                if value >= 2:
                    return False
            row_dict.clear()
                
        column_dict = {}
        for j in range(0, 9):
            for i in range(0, 9):
                if board[i][j] not in column_dict:
                    column_dict[board[i][j]] = 1
                elif board[i][j] != '.':
                    column_dict[board[i][j]] += 1
            
            for value in column_dict.values():
                if value >= 2:
                    return False
            column_dict.clear()

        # [0, 0+0] [0, 1+0] [0, 2+0] # [0, 0+3][0, 1+3][0, 2+3] #[0, 0+3+3]
        # [1, 0] [1, 1] [1, 2]
        # [2, 0] [2, 1] [2, 2]
        
        for m in range(0, 3):
            for n in range(0, 3):
                subbox_dict = {}
                for i in range(m*3, m*3+3):
                    for j in range(n*3, n*3+3):
                        if board[i][j] not in subbox_dict:
                            subbox_dict[board[i][j]] = 1
                        elif board[i][j] != '.':
                            subbox_dict[board[i][j]] += 1
            
                        for value in subbox_dict.values():
                            if value >= 2:
                                return False

                subbox_dict.clear()

        return True
