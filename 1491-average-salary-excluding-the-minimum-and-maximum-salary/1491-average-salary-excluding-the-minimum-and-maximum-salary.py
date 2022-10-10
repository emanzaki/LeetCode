class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        del salary[0]
        del salary[-1]
        sum=0
        for i in salary:
            sum+=i
            
        return sum/len(salary)
        