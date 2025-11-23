class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        boxes_end=[2,5,8]
        boxes_start=[0,3,6]
        row=0
        column=0
        for count in range (0,9):
            sudoko_r=[]
            sudoko_c=[]
            for indexer in range(0,9):
                if board[row][indexer] in sudoko_r and board[row][indexer]!='.':
                    return False
                else:
                    sudoko_r.append(board[row][indexer])
                if board[indexer][column] in sudoko_c and board[indexer][column]!='.':
                    return False
                else:
                    sudoko_c.append(board[indexer][column])
            row=row+1
            column=column+1
        for box_index_end, box_index_start in zip(boxes_end,boxes_start):
            count_boxes=0
            while count_boxes < 3:
                column=boxes_start[count_boxes]
                row=box_index_start
                sudoko_b=[]
                while row<=box_index_end: 
                    temp_column=column
                    while temp_column<column+3:
                        if board[row][temp_column] in sudoko_b and board[row][temp_column]!='.':
                            return False
                        elif row==temp_column:
                            sudoko_b.append(board[row][temp_column])
                        else:
                            sudoko_b.append(board[row][temp_column])
                        temp_column=temp_column+1
                    row=row+1 
                count_boxes=count_boxes+1
        return True


                






        