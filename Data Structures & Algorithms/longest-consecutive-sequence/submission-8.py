class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nm = set(nums)
        max_seq_len = 0

        for num in nm:

            if num - 1 not in nm:
                count = 1
                current = num

                while current + 1 in nm:
                    count += 1
                    current += 1

                max_seq_len = max(max_seq_len, count)

        return max_seq_len