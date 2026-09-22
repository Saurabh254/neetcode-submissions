from collections import  defaultdict
class Solution:

    def get_key(self, word: list[str]) -> int:
        return "".join(sorted([char for char in word]))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            groups[self.get_key(word)].append(word)
        return [value for _, value in groups.items()]
        