class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        target_row = matrix[0]

        # First select which row to perform binary search
        for i in matrix:
            if target <= i[-1]:
                target_row = i
                break
        
        # Perform binary search on target row
        low, high = 0, len(target_row)-1
        while low <= high:
            mid = low + (high-low)//2
            if target == target_row[mid]:
                return True
            else:
                if target > target_row[mid]:
                    low = mid+1
                else:
                    high = mid-1
        return False