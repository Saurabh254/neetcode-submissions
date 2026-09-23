class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prd = 1

        for num in nums:
            result.append(prd)
            prd *= num
        prd =1 

        for i in range(len(nums)-1, -1, -1): 
            result[i] *= prd
            prd *= nums[i]
        return result

        