class Solution:
    def reverseWords(self, s: str) -> str:
        words_reversed = list(reversed(s.split(' ')))
        remove_extra = [w for w in words_reversed if w != '']

        return ' '.join(remove_extra)
