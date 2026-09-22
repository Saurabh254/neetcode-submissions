class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        if len(nums) <= 1:
            return False
        for idx in range(1, len(nums)): 
            if nums[idx-1] == nums[idx]: 
                return True
        return False

        