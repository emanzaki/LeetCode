class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(not(target in nums)):
            nums.append(target)
            nums.sort()
        return nums.index(target)
