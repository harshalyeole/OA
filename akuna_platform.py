# A quantitative trading firm seeks to create a tool for querying the net profit/loss of the firm at anv given time. The tool processes a list of events. each of which can be classified into one of four categories:
# 1.    BUY stock quantity. Signifies the purchase of squanucy> shares of stock <stock> at the market
# 2.    SELL stock auantity. Indicates the sals of quantity> shares of stock <stock> at the market price.
# 3.    CHANGE stock price: Signities a change in the market price of «stock> by <price> amount, wnich can be either positive or negative.
# 4. QUERY: Represents a query for the net profit/loss from the start of trading to the present.
# The tool should return a list of numbers corresponding to each QUERY event.
# Input : ["BUY googl 20", "BUY aapl 50", "CHANGE googl 6", "QUERY","SELL aapl 10", "CHANGE aapl -2", "QUERY"]
# Output : [120,40]

from collections import defaultdict
def getNetProfit(events):
    portfolio = defaultdict(int)
    profit = 0
    results = []
    for event in events:
        if event.startswith('BUY'):
            _, stock, qty = event.split()
            portfolio[stock]+= int(qty)
        elif event.startswith('SELL'):
            _, stock, qty = event.split()
            portfolio[stock]-= int(qty)
        elif event.startswith('CHANGE'):
            _, stock, change = event.split()
            change = int(change)
            if stock in portfolio:
                profit += change * portfolio[stock]
        elif event == 'QUERY' : 
            results.append(profit)
    return results

events = ["BUY googl 20", "BUY aapl 50", "CHANGE googl 6", "QUERY","SELL aapl 10", "CHANGE aapl -2", "QUERY"]
print(getNetProfit(events))