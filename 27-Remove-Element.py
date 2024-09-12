class Solution(object):
    def removeElement(self, nums, val):
        for x in range(len(nums)-1,-1,-1):
            if nums[x] == val:
                del nums[x]
        return len(nums)
        