class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1 if nums else 0 
        modified_nums = sorted(set(nums))
        mx, count = 0, 1
        for i in range(1, len(modified_nums)): 
            if modified_nums[i] - modified_nums[i-1] != 1:
                mx = max(mx, count)
                count = 1
            else:
                count += 1
        
        return max(mx, count)