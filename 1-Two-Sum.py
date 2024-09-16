class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2:
            return [0,1]
        arr=[]
        for x in range(len(nums)):
            min=target-nums[x]
            if(min in nums[x+1:]):
                arr.append(x)
                arr.append(nums[x+1:].index(min)+x+1) #searching for the another index in the rest of the list
            if len(arr) ==2:
                break
        return arr


