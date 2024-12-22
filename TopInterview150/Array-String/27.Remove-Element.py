# Remove Element


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = [num for num in nums if num != val]
        nums.clear()
        nums.extend(result)

        return len(result)
