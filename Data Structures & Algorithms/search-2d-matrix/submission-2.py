class Solution:
    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n - 1
        while start <= end:
            mid = (start + end) // 2
            row = mid // n
            col = mid % n
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                start = mid + 1
            else:
                end = mid - 1
        return False 