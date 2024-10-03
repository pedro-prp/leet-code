class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_dict = {}

        for num in nums:
            key = str(num)
            if key in majority_dict:
                majority_dict[key] += 1
            else:
                majority_dict[key] = 1

        sorted_dict = dict(
            sorted(majority_dict.items(), key=lambda item: item[1], reverse=True)
        )

        return int(next(iter(sorted_dict)))
