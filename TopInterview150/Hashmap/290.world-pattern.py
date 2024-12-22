class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        found_dict = {}
        found_pass = {}
        s = s.split(' ')

        if len(pattern) != len(s):
            return False

        for index, c in enumerate(pattern):

            if c in found_dict:
                if found_dict[c] != s[index]:
                    return False
            else:
                if s[index] in found_pass:
                    return False
                found_dict[c] = s[index]
                found_pass[s[index]] = c
        
        return True
