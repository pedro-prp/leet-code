class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        normalized_s = sorted(s)
        normalized_t = sorted(t)

        if normalized_s == normalized_t:
            return True
        
        return False
