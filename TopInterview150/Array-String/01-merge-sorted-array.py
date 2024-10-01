# Merge Sorted Array


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        index_1, index_2 = 0, 0
        result = []

        while index_1 < m and index_2 < n:
            if nums1[index_1] < nums2[index_2]:
                result.append(nums1[index_1])
                index_1 += 1
            else:
                result.append(nums2[index_2])
                index_2 += 1

        while index_1 < m:
            result.append(nums1[index_1])
            index_1 += 1

        while index_2 < n:
            result.append(nums2[index_2])
            index_2 += 1

        nums1.clear()
        nums1.extend(result)
