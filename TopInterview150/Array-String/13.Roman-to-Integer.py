class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        result = roman_values[s[-1]]
        
        for i in range(len(s) - 2, -1, -1):
            if roman_values[s[i]] >= roman_values[s[i + 1]]:
                result += roman_values[s[i]]
            else:
                result -= roman_values[s[i]]
        
        return result
