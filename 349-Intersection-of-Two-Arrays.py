class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(nums1)
        num2 = set(nums2)
        arr =[]
        for x in nums1:
            if x in nums2:
                arr.append(x)
        return set(arr)