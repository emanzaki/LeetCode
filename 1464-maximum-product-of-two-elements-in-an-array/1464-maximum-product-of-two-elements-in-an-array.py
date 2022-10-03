class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        temp = (nums[0]-1)*(nums[1]-1)
        return temp
