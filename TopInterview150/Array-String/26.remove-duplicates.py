# Remove Duplicates from Sorted Array


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = list(set(nums))
        unique.sort()
        nums.clear()
        nums.extend(unique)

        return len(nums)
