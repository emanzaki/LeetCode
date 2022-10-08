class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        arr = []
        for i in range(len(prices)):

            if (i < len(prices)-1):
                if prices[i] <= prices[i+1]:
                    arr.append(prices[i])
                    continue
                else:
                    arr.append(prices[i])
                    profit += arr[-1]-arr[0]
                    arr = []
            else:
                arr.append(prices[i])
                profit += arr[-1]-arr[0]

        return profit