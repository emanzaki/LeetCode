class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            if x not in dic:
                dic[x] = 0
            dic[x] = dic[x]+1
        num = sorted(dic.items(), key=lambda x: x[1], reverse=True)[0][0]
        return num

