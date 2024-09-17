class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        arr =[]
        for x in nums1:
            if x in nums2:
                arr.append(x)
        return set(arr)