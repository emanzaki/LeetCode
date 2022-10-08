class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=0
        for x in range (k):
            z=nums[-1]
            del nums[-1]
            nums.insert(0,z)
            
        