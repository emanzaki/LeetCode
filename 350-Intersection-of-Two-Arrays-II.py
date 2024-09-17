class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr =[]
        for x in nums1:
            if x in nums2:
                nums2.remove(x)
                arr.append(x)
                    
        return arr