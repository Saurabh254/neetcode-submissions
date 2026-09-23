class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string


    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0 
        result = []
        while i<n:
            j = i
            length = ""
            while s[j] != '#': 
                length += s[j]
                j+=1
            
            j+= 1

            result.append(s[j:j+int(length)])

            
            i = j + int(length)
        return result



