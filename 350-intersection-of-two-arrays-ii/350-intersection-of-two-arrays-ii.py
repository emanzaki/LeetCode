class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        if(len(nums1)<len(nums2)):
            for i in nums1:
                if i in nums2 :
                    arr.append(i)
                    nums2.remove(i)
                    
        else:
            for i in nums2:
                if i in nums1:
                    arr.append(i)
                    nums1.remove(i)
        
        return arr
                    
        