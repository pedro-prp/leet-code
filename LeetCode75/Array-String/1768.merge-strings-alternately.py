class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)

        pos_w1 = 0
        pos_w2 = 0

        str_built = []

        while pos_w1 < len_word1 and pos_w2 < len_word2:
            str_built.append(word1[pos_w1])
            str_built.append(word2[pos_w2])

            pos_w1 += 1
            pos_w2 += 1

        while pos_w1 < len_word1:
            str_built.append(word1[pos_w1])
            pos_w1 += 1

        while pos_w2 < len_word2:
            str_built.append(word2[pos_w2])
            pos_w2 += 1

        return "".join(str_built)
