class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = str(n)
        sum, prod = 0, 1
        for i in x:
            sum += int(i)
            prod *= int(i)

        return prod-sum

            