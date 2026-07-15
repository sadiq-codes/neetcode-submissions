class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = row1
        bottom = row2
        left = col1
        right = col2
        
        total = 0
        while top <= bottom and left <= right:

            for col in range(left, right + 1):
                total += self.matrix[top][col]
            top += 1

            for row in range(top, bottom + 1):
                total += self.matrix[row][right]
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    total += self.matrix[bottom][col]
            bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    total += self.matrix[row][left]
            left += 1
        
        return total

            
            

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)