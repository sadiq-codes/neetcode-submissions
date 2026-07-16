class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        blockDup = [set() for val in range(len(board))]
        print(blockDup)
        for row in range(len(board)):
            rowDup = set()
            colDup = set()
            for col in range(len(board[1])):
                if board[row][col] != "." and board[row][col] in rowDup:
                    return False
                rowDup.add(board[row][col])
                print("rowDup", rowDup)
                if board[col][row] != "." and board[col][row] in colDup:
                    return False
                colDup.add(board[col][row])
                print("colDup", colDup)

                print((row // 3) * 3 + (col // 3))
                blockId = (row // 3) * 3 + (col // 3)
                if board[row][col] != "." and board[row][col] in blockDup[blockId]:
                    return False
                blockDup[blockId].add(board[row][col])
                print(blockDup[blockId])
        return True
                

