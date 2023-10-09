def maxProfit(prices):
  '''
  Using kadanse Algorithm
  with sliding window technique
  move the window start to the lowest price
  and subract each price with lowest to find max profit
  '''
  max_profit = 0
  lowest = prices[0]  # assuming
  for price in prices:
    if price < lowest:
      lowest = price
    max_profit = max(max_profit, price - lowest)
  return max_profit


res = maxProfit([100, 200, 50, 78, 10, 68])

print(res)
