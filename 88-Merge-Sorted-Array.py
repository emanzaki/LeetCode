class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        \\\
        Do not return anything, modify nums1 in-place instead.
        \\\
        nums1.extend( nums2) 
        while(m+n < len(nums1)):
            nums1.remove(0)
        nums1.sort()