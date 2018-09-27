#!/usr/bin/python
'''
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
get_max_profit(stock_prices_yesterday)
Returns 6 (buying for $5 and selling for $11)
'''

def get_max_profit(stock_prices_yesterday):
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index in range(1, len(stock_prices_yesterday)):
        potential_profit = stock_prices_yesterday[index] - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, stock_prices_yesterday[index])
    return max_profit

apple_stock =  [10,7,5,8,11,9]
print get_max_profit(apple_stock)

bitcoin = [20, 16, 12, 4]
print get_max_profit(bitcoin)
