class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hax_table = {}

        for num in nums:
            if num in hax_table:
                hax_table[num] += 1
            else:
                hax_table[num] = 1
        
        print(hax_table.items())

        for key, value in hax_table.items():
            if value == 1:
                return key
