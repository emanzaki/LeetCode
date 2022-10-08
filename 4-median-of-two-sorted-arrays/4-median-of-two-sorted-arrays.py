class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        median = 0
        z = 0
        nums1[len(nums1):] = nums2
        nums1.sort()
        x = len(nums1)
        if x == 1:
            return nums1[0]
        elif x % 2 == 0:
            z = (nums1[x//2]+nums1[(x//2)-1])/2
            median = z
            return median

        else:
            z = (x-1)//2
            median = nums1[z]
            return median