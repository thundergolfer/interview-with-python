# Stocks Maximum Sub-Array Problem

You've been offered the opportunity to invest in a stock, but the opportunity has some conditions.

1. You are allowed to buy one unit of stock only one time and then sell it all at a later date.
2. You can only buy and sell at close of trading.
3. You are allowed to know the future price of the stock.


Your goal is to maximise your profit from this single trade, which comes down to finding the greatest difference between two closing prices over a given period.
This period has a `start` and an `end`.

We represent prices for this solution as the price[i-1] - price[i] for price[i]. This is the *difference*, or price movement.

```python
# where returned values x, y are the indexes of the days to buy sell
find-max-subarray( prices, 0, 132) # > 3, 45
```
