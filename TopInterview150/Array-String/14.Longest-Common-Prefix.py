class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_list = sorted(strs, key=len)

        checker = new_list[0]

        cont = 0
        while cont < len(checker):
            for s in strs:
                if s[cont] != checker[cont]:
                    return checker[:cont]

            cont += 1

        return checker[:cont]
