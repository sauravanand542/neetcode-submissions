class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = [0]*26

        for c in s:
            count[ord("a")-ord(c)]  += 1
        
        for c in t:
            count[ord("a")-ord(c)] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True

        