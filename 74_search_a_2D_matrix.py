# https://leetcode.com/problems/search-a-2d-matrix/

# This solution is beautiful
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        r = len(matrix)

        i = 0
        j = len(matrix[0])-1

        while i < r and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        
        return False

# T = O(M + N)
# S = O(1)