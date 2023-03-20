# Given an array where the element at the index i represents the price 
# of a stock on day i, find the maximum profit that you can gain by 
# buying the stock once and then selling it.

def max_profit(stock_prices):
    left, right, max_profit = 0, 1, 0

    while right < len(stock_prices):
        if stock_prices[left] > stock_prices[right]:
            left = right

        max_profit = max(max_profit, stock_prices[right] - stock_prices[left])
        right += 1

    return max_profit

tests = [[1,2,4,2,5,7,2,4,9,0,9], [7,1,5,3,6,4], [7,6,4,3,1]]

for test in tests:
    print(f"input : {test}, output: {max_profit(test)}")