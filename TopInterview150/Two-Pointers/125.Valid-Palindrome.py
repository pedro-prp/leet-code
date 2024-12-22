class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalpha() or c.isdigit()).lower()

        if s[::-1] == s:
            return True
        else:
            return False
