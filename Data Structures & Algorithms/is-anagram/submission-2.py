class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        
        s = "".join(sorted([char for char in s]))
        t = "".join(sorted([char for char in t]))
        for i in range(len(s)): 
            if s[i] != t[i]: 
                return False

        return True 


        