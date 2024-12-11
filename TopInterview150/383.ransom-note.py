def count_letters(str):
    freq_dict = dict()
    for c in str:
        if c in freq_dict:
            freq_dict[c] += 1
        else:
            freq_dict[c] = 1

    return freq_dict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_ransom = count_letters(ransomNote)
        freq_magazine = count_letters(magazine)

        for key, value in freq_ransom.items():

            if (key not in freq_magazine) or (freq_magazine[key] < value):
                return False

        return True
