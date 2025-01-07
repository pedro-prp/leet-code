class Solution:
    def reverse(self, x: int) -> int:
        converted = int(str(x).replace("-", "")[::-1])

        if converted >= pow(2, 31) - 1:
            return 0
        if x < 0:
            return converted * (-1)
        else:
            return converted
