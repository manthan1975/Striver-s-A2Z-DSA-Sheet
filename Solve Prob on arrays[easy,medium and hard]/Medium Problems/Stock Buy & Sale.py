# Time Complexity: O(n)
# Space Complexity: O(1)

def stockBuy_sale(prices):
    maxprofit = 0
    bestBuy = prices[0]

    for i in range(1,len(prices)):
        if (prices[i] > bestBuy):
            maxprofit = max(maxprofit,prices[i] - bestBuy)

        bestBuy = min(bestBuy,prices[i])

    return maxprofit

if __name__  == "__main__":
    prices = [7,1,4,5,6,3]
    print(stockBuy_sale(prices))