class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr=set(nums)
        for i in arr:
            nums.remove(i)
            if i not in nums:
                return i