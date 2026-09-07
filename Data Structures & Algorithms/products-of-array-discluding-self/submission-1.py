class Solution:
    #[1, 1, 2, 8]
    #[48, 24, 6, 1]

    #[1, -1, 0, 0, 0]
    #[0, 6, 6, 3, 1]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        result = [1] * n 
        for i in range(n):
            result[i] = prefix
            prefix = prefix * nums[i]
        
        suffix = 1
        for i in range(n-1,-1,-1):
            result[i] = suffix * result[i]
            suffix = suffix * nums[i]
        return result


            