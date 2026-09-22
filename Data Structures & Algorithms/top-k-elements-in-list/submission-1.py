from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = defaultdict(int)
        for num in nums:
            groups[num] += 1

        return [key[0] for key in sorted(groups.items(), key=lambda x: -x[1])][:k]
        

        
        